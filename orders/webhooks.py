# The webhooks.py file processes asynchronous payment notifications sent
# directly from Stripe to the application. Unlike the normal checkout
# process, webhook requests are server-to-server communications and do
# not depend upon the customer's browser remaining open after payment.
#
# This design improves reliability because an order can still be created
# if the customer closes their browser, loses their internet connection
# or never reaches the checkout success page.
#
# Every webhook request is cryptographically verified using Stripe's
# signing secret before any order or stock information is modified,
# protecting the application from unauthorised requests.

"""
Stripe webhook handler.

Stripe sends a server-to-server POST to this endpoint whenever a payment event
occurs (e.g. payment_intent.succeeded). Because this arrives independently of the
customer's browser, it guarantees the order is recorded even if the customer
closes their browser after paying but before the success page loads.

Security: every request is verified against the endpoint's signing secret
(STRIPE_WH_SECRET) so that only genuine Stripe events are acted on.
"""

# Import JSON support so the cart stored within Stripe metadata can be
# reconstructed into Python objects.
import json

# Import Stripe's Python SDK for webhook verification.
import stripe

# Import project settings containing the Stripe secret keys.
from django.conf import settings

# Import HttpResponse so appropriate HTTP status codes can be returned
# to Stripe after processing each webhook event.
from django.http import HttpResponse

# Disable CSRF protection because webhook requests originate from Stripe's
# servers rather than from forms submitted by authenticated users.
from django.views.decorators.csrf import csrf_exempt

# Restrict this endpoint to POST requests because Stripe webhooks always
# use the HTTP POST method.
from django.views.decorators.http import require_POST

# Import Product so stock levels can be updated after successful payment.
from shop.models import Product

# Import the order models used when reconstructing completed purchases.
from .models import Order, OrderLineItem


@require_POST
@csrf_exempt
def stripe_webhook(request):
    """
    Receive, authenticate and process Stripe webhook events.

    Every incoming request is validated using Stripe's webhook signing
    secret before any payment information is trusted.
    """

    # Retrieve the webhook signing secret and configure the Stripe SDK.
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Retrieve the raw request body exactly as Stripe sent it. Signature
    # verification requires the original unmodified payload.
    payload = request.body

    # Retrieve the Stripe-Signature header supplied with the request.
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    # Verify that the request genuinely originated from Stripe.
    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            wh_secret
        )

    # Reject malformed request bodies.
    except ValueError:
        return HttpResponse(
            'Invalid payload',
            status=400
        )

    # Reject requests whose cryptographic signature does not match the
    # configured webhook secret.
    except stripe.error.SignatureVerificationError:
        return HttpResponse(
            'Invalid signature',
            status=400
        )

    # Process only the webhook events required by this application.
    if event['type'] == 'payment_intent.succeeded':

        # Extract the successful Payment Intent object.
        intent = event['data']['object']

        # Delegate the order creation process to a dedicated helper
        # function to keep this view concise and maintainable.
        _handle_payment_succeeded(intent)

    # Acknowledge every recognised webhook so Stripe does not continue
    # retrying delivery.
    return HttpResponse(status=200)


def _handle_payment_succeeded(intent):
    """
    Validate a successful payment and reconstruct the customer's order.

    Multiple validation checks are performed before any database records
    are created to ensure that only genuine and internally consistent
    payments are fulfilled.
    """

    # Retrieve the unique Stripe Payment Intent identifier.
    pid = intent['id']

    # Prevent duplicate orders if Stripe retries delivery of the same
    # webhook event. This makes the webhook idempotent.
    if Order.objects.filter(
        stripe_payment_intent_id=pid
    ).exists():
        return

    # Confirm that Stripe itself considers the payment successful before
    # proceeding.
    status = (
        intent['status']
        if 'status' in intent
        else None
    )

    if status != 'succeeded':
        return

    # Retrieve the metadata attached to the Payment Intent during the
    # checkout process.
    metadata = (
        intent['metadata']
        if 'metadata' in intent
        else {}
    )

    def meta(key, default=''):
        """
        Safely retrieve a metadata value.

        Missing or malformed metadata returns a default value rather than
        raising an exception.
        """
        try:
            return metadata[key]
        except (KeyError, TypeError):
            return default

    # Retrieve the serialised shopping cart stored within Stripe.
    cart_json = meta('cart', '{}')

    # Convert the JSON string back into a Python dictionary.
    try:
        cart = json.loads(cart_json)

    except (ValueError, TypeError):
        cart = {}

    # Without a valid cart there is nothing to reconstruct.
    if not cart:
        return

    # Build the order line items and calculate the expected subtotal
    # before creating any database records.
    line_items = []
    subtotal = 0

    for item_id, quantity in cart.items():

        # Ignore products that no longer exist.
        try:
            product = Product.objects.get(pk=item_id)

        except Product.DoesNotExist:
            continue

        line_items.append((product, quantity))
        subtotal += quantity * product.price

    # Stop processing if no valid products remain.
    if not line_items:
        return

    # Calculate the amount that should have been charged using the same
    # calculation as the checkout view.
    expected_amount = round(subtotal * 100)

    # Retrieve the amount confirmed by Stripe.
    charged_amount = (
        intent['amount_received']
        if 'amount_received' in intent
        else (
            intent['amount']
            if 'amount' in intent
            else None
        )
    )

    # Retrieve the payment currency.
    charged_currency = (
        intent['currency']
        if 'currency' in intent
        else ''
    ).lower()

    # Refuse to fulfil the order if the amount paid differs from the
    # expected cart total.
    if charged_amount != expected_amount:
        return

    # Refuse to fulfil payments made using an unexpected currency.
    if charged_currency != settings.STRIPE_CURRENCY.lower():
        return

    # Import transaction support only where required.
    from django.db import transaction

    # Create the order and update stock within one atomic transaction so
    # all related database changes either succeed together or are rolled
    # back together.
    with transaction.atomic():

        # Reconstruct the original order using the metadata saved during
        # checkout.
        order = Order(
            order_number=pid,
            full_name=meta('full_name'),
            email=meta('email'),
            phone=meta('phone'),
            address_line1=meta('address_line1'),
            address_line2=meta('address_line2'),
            town_city=meta('town_city'),
            postcode=meta('postcode'),
            country=meta('country'),
            stripe_payment_intent_id=pid,
            subtotal=subtotal,
            total=subtotal,
        )

        order.save()

        # Recreate each purchased line item.
        for product, quantity in line_items:

            OrderLineItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price,
            )

            # Reduce the available stock while preventing negative values.
            new_stock = max(
                product.stock - quantity,
                0
            )

            Product.objects.filter(
                pk=product.pk
            ).update(stock=new_stock)
