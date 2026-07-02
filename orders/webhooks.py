"""
Stripe webhook handler.

Stripe sends a server-to-server POST to this endpoint whenever a payment event
occurs (e.g. payment_intent.succeeded). Because this arrives independently of the
customer's browser, it guarantees the order is recorded even if the customer
closes their browser after paying but before the success page loads.

Security: every request is verified against the endpoint's signing secret
(STRIPE_WH_SECRET) so that only genuine Stripe events are acted on.
"""
import json

import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from shop.models import Product
from .models import Order, OrderLineItem


@require_POST
@csrf_exempt
def stripe_webhook(request):
    """Receive and verify Stripe webhook events."""
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    # 1. Verify the event really came from Stripe.
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError:
        # Malformed payload
        return HttpResponse('Invalid payload', status=400)
    except stripe.error.SignatureVerificationError:
        # Signature didn't match our secret -> reject
        return HttpResponse('Invalid signature', status=400)

    # 2. Handle the events we care about.
    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        _handle_payment_succeeded(intent)

    # Any other event type: acknowledge so Stripe stops retrying.
    return HttpResponse(status=200)


def _handle_payment_succeeded(intent):
    """Create the order for a successful payment, if it doesn't exist yet."""
    pid = intent['id']

    # Idempotency: if an order already exists for this PaymentIntent (because the
    # normal checkout flow already created it), do nothing.
    if Order.objects.filter(stripe_payment_intent_id=pid).exists():
        return

    metadata = intent['metadata'] if 'metadata' in intent else {}
    # metadata is a StripeObject; normalise access
    def meta(key, default=''):
        try:
            return metadata[key]
        except (KeyError, TypeError):
            return default
    cart_json = meta('cart', '{}')
    try:
        cart = json.loads(cart_json)
    except (ValueError, TypeError):
        cart = {}

    if not cart:
        # Nothing to build an order from.
        return

    # Rebuild the order from the metadata Stripe stored on the PaymentIntent.
    order = Order(
        order_number=pid,  # use the intent id as a stable order number here
        full_name=meta('full_name'),
        email=meta('email'),
        phone=meta('phone'),
        address_line1=meta('address_line1'),
        address_line2=meta('address_line2'),
        town_city=meta('town_city'),
        postcode=meta('postcode'),
        country=meta('country'),
        stripe_payment_intent_id=pid,
    )

    from django.db import transaction
    subtotal = 0
    with transaction.atomic():
        order.subtotal = 0
        order.total = 0
        order.save()
        for item_id, quantity in cart.items():
            try:
                product = Product.objects.get(pk=item_id)
            except Product.DoesNotExist:
                continue
            OrderLineItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price,
            )
            subtotal += quantity * product.price
            new_stock = max(product.stock - quantity, 0)
            Product.objects.filter(pk=product.pk).update(stock=new_stock)
        order.subtotal = subtotal
        order.total = subtotal
        order.save()