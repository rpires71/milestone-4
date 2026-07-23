"""Tests for Stripe webhook signature verification and order creation."""
import hashlib
import hmac
import json
import time

from django.test import TestCase, override_settings
from django.urls import reverse

from orders.models import Order
from shop.models import Product, ProductCategory

WH_SECRET = 'whsec_test_secret_for_tests'


def _sign(payload):
    """Produce a valid Stripe-Signature header for the given payload."""
    ts = int(time.time())
    signed = f'{ts}.{payload}'
    sig = hmac.new(WH_SECRET.encode(), signed.encode(), hashlib.sha256).hexdigest()
    return f't={ts},v1={sig}'


def _event(pid, cart):
    return json.dumps({
        'id': 'evt_' + pid,
        'object': 'event',
        'api_version': '2024-01-01',
        'type': 'payment_intent.succeeded',
        'data': {'object': {
            'id': pid,
            'object': 'payment_intent',
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
        }},
    })


@override_settings(STRIPE_WH_SECRET=WH_SECRET)
class StripeWebhookTest(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(name='Equipment', slug='equipment-wh')
        self.product = Product.objects.create(
            category=self.category, name='WH Kettlebell', slug='wh-kettlebell',
            description='Test.', price=20.00, stock=10,
        )

    def test_valid_event_creates_order(self):
        payload = _event('pi_valid', {str(self.product.id): 2})
        response = self.client.post(
            reverse('stripe_webhook'), data=payload,
            content_type='application/json', HTTP_STRIPE_SIGNATURE=_sign(payload),
        )
        self.assertEqual(response.status_code, 200)
        order = Order.objects.get(stripe_payment_intent_id='pi_valid')
        self.assertEqual(order.line_items.count(), 1)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 8)  # 10 - 2

    def test_bad_signature_rejected(self):
        payload = _event('pi_bad', {str(self.product.id): 1})
        response = self.client.post(
            reverse('stripe_webhook'), data=payload,
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE='t=1,v1=deadbeef',
        )
        self.assertEqual(response.status_code, 400)
        self.assertFalse(Order.objects.filter(stripe_payment_intent_id='pi_bad').exists())

    def test_duplicate_event_is_idempotent(self):
        payload = _event('pi_dupe', {str(self.product.id): 1})
        header = _sign(payload)
        self.client.post(reverse('stripe_webhook'), data=payload,
                         content_type='application/json', HTTP_STRIPE_SIGNATURE=header)
        # Fire the same event again
        self.client.post(reverse('stripe_webhook'), data=payload,
                         content_type='application/json', HTTP_STRIPE_SIGNATURE=_sign(payload))
        self.assertEqual(
            Order.objects.filter(stripe_payment_intent_id='pi_dupe').count(), 1
        )

    def test_webhook_skips_when_order_already_exists(self):
        # Simulate the normal checkout flow having already created the order.
        Order.objects.create(
            order_number='EXISTING1', full_name='Normal', email='n@e.com',
            address_line1='1 St', town_city='T', postcode='P', country='GB',
            subtotal=20, total=20, stripe_payment_intent_id='pi_exists',
        )
        before = Order.objects.count()
        payload = _event('pi_exists', {str(self.product.id): 3})
        self.client.post(reverse('stripe_webhook'), data=payload,
                         content_type='application/json', HTTP_STRIPE_SIGNATURE=_sign(payload))
        self.assertEqual(Order.objects.count(), before)  # no duplicate
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 10)  # stock not double-deducted
