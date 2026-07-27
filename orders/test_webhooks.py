# The test_webhooks.py file contains automated tests for the Stripe webhook
# functionality used by the Orders application. These tests verify that
# webhook requests are authenticated correctly, valid payments create orders,
# duplicate events do not create duplicate records, stock is updated safely
# and payments with incorrect amounts are not fulfilled.
#
# Testing this behaviour is important because webhook processing occurs
# independently of the browser-based checkout flow. The application must
# therefore validate each event before changing order or stock data.

"""Tests for Stripe webhook signature verification and order creation."""

# Import hashing and message-authentication utilities so the tests can
# reproduce the signature format used by Stripe webhook requests.
import hashlib
import hmac

# Import JSON support for creating webhook payloads and serialising cart data.
import json

# Import time so each test signature can include a current timestamp.
import time

# Import Django's TestCase for isolated database tests and override_settings
# so the test webhook secret can temporarily replace the project setting.
from django.test import TestCase, override_settings

# Import reverse so the webhook URL can be resolved by name rather than
# hard-coded, improving maintainability if the route changes.
from django.urls import reverse

# Import the models required to verify order creation and stock changes.
from orders.models import Order
from shop.models import Product, ProductCategory


# Define a test-only webhook secret. This avoids using real Stripe credentials
# while still allowing the tests to verify the signature-validation logic.
WH_SECRET = 'whsec_test_secret_for_tests'


def _sign(payload):
    """
    Produce a valid Stripe-Signature header for the supplied payload.

    This helper mirrors Stripe's signing process so that tests can submit
    authenticated webhook requests without contacting the external API.
    """

    # Generate the timestamp included in Stripe's signed webhook message.
    ts = int(time.time())

    # Combine the timestamp and raw payload using Stripe's expected format.
    signed = f'{ts}.{payload}'

    # Create an HMAC SHA-256 digest using the test webhook secret.
    sig = hmac.new(
        WH_SECRET.encode(),
        signed.encode(),
        hashlib.sha256
    ).hexdigest()

    # Return the header value in the same structure used by Stripe.
    return f't={ts},v1={sig}'


def _event(pid, cart, amount, currency='gbp', status='succeeded'):
    """
    Build a representative Stripe payment_intent.succeeded webhook event.

    Centralising the payload structure reduces duplication across the tests
    and allows individual scenarios to vary only the payment identifier,
    cart contents, amount, currency or payment status.
    """

    # Serialise the simulated Stripe event into JSON because webhook
    # requests send their data as a JSON-formatted HTTP request body.
    return json.dumps({
        'id': 'evt_' + pid,
        'object': 'event',
        'api_version': '2024-01-01',
        'type': 'payment_intent.succeeded',
        'data': {
            'object': {
                'id': pid,
                'object': 'payment_intent',
                'status': status,
                'amount': amount,
                'amount_received': amount,
                'currency': currency,

                # Store the cart and delivery details in metadata so the
                # webhook handler can reconstruct the order if required.
                'metadata': {
                    'cart': json.dumps(cart),
                    'full_name': 'Webhook User',
                    'email': 'wh@example.com',
                    'phone': '',
                    'address_line1': '1 Hook Street',
                    'address_line2': '',
                    'town_city': 'Webville',
                    'postcode': 'WH1 1WH',
                    'country': 'GB',
                    'username': '',
                },
            }
        },
    })


# Replace the production Stripe webhook secret with the test secret for every
# test in this class. This keeps the tests isolated from external credentials.
@override_settings(STRIPE_WH_SECRET=WH_SECRET)
class StripeWebhookTest(TestCase):
    """
    Verify the security, reliability and idempotency of Stripe webhook
    processing within the Orders application.
    """

    def setUp(self):
        """
        Create reusable catalogue data before each test.

        Django provides a clean test database for every test method, ensuring
        that tests remain independent and cannot affect one another.
        """

        # Create a category required by the test product.
        self.category = ProductCategory.objects.create(
            name='Equipment',
            slug='equipment-wh'
        )

        # Create an available product with known price and stock values so
        # each test can verify totals and inventory changes predictably.
        self.product = Product.objects.create(
            category=self.category,
            name='WH Kettlebell',
            slug='wh-kettlebell',
            description='Test.',
            price=20.00,
            stock=10,
        )

    def test_valid_event_creates_order(self):
        """
        Confirm that a correctly signed and fully paid webhook event creates
        one order, adds its line item and reduces the product stock.
        """

        # Arrange: create a payload for two £20 products, producing a
        # correctly matched Stripe amount of 4000 pence.
        payload = _event(
            'pi_valid',
            {str(self.product.id): 2},
            amount=4000
        )

        # Act: submit the simulated webhook request with a valid signature.
        response = self.client.post(
            reverse('stripe_webhook'),
            data=payload,
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE=_sign(payload),
        )

        # Assert: a successfully processed webhook should return HTTP 200.
        self.assertEqual(response.status_code, 200)

        # Confirm that the order was saved using the Stripe Payment Intent ID.
        order = Order.objects.get(
            stripe_payment_intent_id='pi_valid'
        )

        # Confirm that the order contains one line item for the selected
        # product and quantity.
        self.assertEqual(order.line_items.count(), 1)

        # Reload the product because the webhook changed its database values.
        self.product.refresh_from_db()

        # Confirm that purchasing two units reduced stock from 10 to 8.
        self.assertEqual(self.product.stock, 8)

    def test_bad_signature_rejected(self):
        """
        Confirm that a webhook with an invalid signature is rejected and
        cannot create an order.
        """

        # Arrange: build an otherwise valid payment event.
        payload = _event(
            'pi_bad',
            {str(self.product.id): 1},
            amount=2000
        )

        # Act: submit the event using a deliberately invalid signature.
        response = self.client.post(
            reverse('stripe_webhook'),
            data=payload,
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE='t=1,v1=deadbeef',
        )

        # Assert: invalid authentication should produce HTTP 400.
        self.assertEqual(response.status_code, 400)

        # Confirm that untrusted webhook data did not create an order.
        self.assertFalse(
            Order.objects.filter(
                stripe_payment_intent_id='pi_bad'
            ).exists()
        )

    def test_duplicate_event_is_idempotent(self):
        """
        Confirm that processing the same Stripe event more than once creates
        only one order.

        Stripe may retry webhook delivery, so the handler must be idempotent
        and avoid duplicating customer purchases.
        """

        # Arrange: build one valid payment event and signature.
        payload = _event(
            'pi_dupe',
            {str(self.product.id): 1},
            amount=2000
        )
        header = _sign(payload)

        # Act: process the event for the first time.
        self.client.post(
            reverse('stripe_webhook'),
            data=payload,
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE=header
        )

        # Act again: simulate Stripe retrying the same event.
        self.client.post(
            reverse('stripe_webhook'),
            data=payload,
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE=_sign(payload)
        )

        # Assert: only one order should exist for the Payment Intent.
        self.assertEqual(
            Order.objects.filter(
                stripe_payment_intent_id='pi_dupe'
            ).count(),
            1
        )

    def test_webhook_skips_when_order_already_exists(self):
        """
        Confirm that the webhook does not recreate an order that has already
        been generated by the normal checkout flow.
        """

        # Arrange: simulate an order already created after checkout.
        Order.objects.create(
            order_number='EXISTING1',
            full_name='Normal',
            email='n@e.com',
            address_line1='1 St',
            town_city='T',
            postcode='P',
            country='GB',
            subtotal=20,
            total=20,
            stripe_payment_intent_id='pi_exists',
        )

        # Record the number of orders before webhook processing.
        before = Order.objects.count()

        # Build a webhook referencing the same Payment Intent.
        payload = _event(
            'pi_exists',
            {str(self.product.id): 3},
            amount=6000
        )

        # Act: submit the webhook event.
        self.client.post(
            reverse('stripe_webhook'),
            data=payload,
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE=_sign(payload)
        )

        # Assert: the order count should remain unchanged.
        self.assertEqual(Order.objects.count(), before)

        # Reload the product after webhook processing.
        self.product.refresh_from_db()

        # Confirm that stock was not deducted a second time.
        self.assertEqual(self.product.stock, 10)

    def test_amount_mismatch_creates_no_order(self):
        """
        Confirm that a payment is not fulfilled when the Stripe amount does
        not match the total calculated from the cart.
        """

        # Arrange: the cart total should be £40, but the event reports only
        # £20. This represents an invalid or inconsistent payment.
        payload = _event(
            'pi_wrong',
            {str(self.product.id): 2},
            amount=2000
        )

        # Act: submit the correctly signed but financially invalid event.
        response = self.client.post(
            reverse('stripe_webhook'),
            data=payload,
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE=_sign(payload),
        )

        # Assert: return HTTP 200 to acknowledge receipt and prevent repeated
        # Stripe retries, while still refusing to fulfil the order.
        self.assertEqual(response.status_code, 200)

        # Confirm that no order was created from the mismatched payment.
        self.assertFalse(
            Order.objects.filter(
                stripe_payment_intent_id='pi_wrong'
            ).exists()
        )

        # Reload the product to inspect its current stock.
        self.product.refresh_from_db()

        # Confirm that stock remains unchanged because the order was not
        # fulfilled.
        self.assertEqual(self.product.stock, 10)
