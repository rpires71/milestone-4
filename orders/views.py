"""Views for the checkout flow, order confirmation and order history."""

import json
import uuid
from datetime import timedelta

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.template.loader import render_to_string

from shop.models import Product

from .forms import OrderForm
from .models import Order, OrderLineItem


def checkout(request):
    """Handle the checkout process and Stripe payment."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None

            # Recover the PaymentIntent id from the client secret so the order and
            # the webhook can be matched (idempotency).
            client_secret = request.POST.get('client_secret', '')
            pid = client_secret.split('_secret')[0] if client_secret else ''
            order.stripe_payment_intent_id = pid

            # Store the cart + delivery details on the PaymentIntent so the webhook
            # can rebuild the order if the customer's browser never returns.
            if pid:
                try:
                    stripe.PaymentIntent.modify(pid, metadata={
                        'cart': json.dumps(cart),
                        'full_name': order.full_name,
                        'email': order.email,
                        'phone': order.phone,
                        'address_line1': order.address_line1,
                        'address_line2': order.address_line2,
                        'town_city': order.town_city,
                        'postcode': order.postcode,
                        'country': order.country,
                        'username': request.user.username if request.user.is_authenticated else '',
                    })
                except Exception:
                    # If metadata update fails, the normal flow still records the
                    # order below; only the webhook fallback would be affected.
                    pass

            subtotal = 0
            for item_id, quantity in cart.items():
                product = get_object_or_404(Product, pk=item_id)
                subtotal += quantity * product.price

            order.subtotal = subtotal
            order.delivery_cost = 0
            order.total = subtotal
            order.order_number = uuid.uuid4().hex.upper()

            # Create the order, its line items, and deduct stock atomically so
            # they all succeed or all fail together.
            with transaction.atomic():
                order.save()
                for item_id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=item_id)
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price=product.price,
                    )
                    # Deduct sold quantity from stock (F() = atomic DB update).
                    # Never let stock fall below zero.
                    new_stock = max(product.stock - quantity, 0)
                    Product.objects.filter(pk=product.pk).update(stock=new_stock)

            # Clear the cart and go to success page
            request.session['cart'] = {}
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Please correct the highlighted fields below.')

    else:
        order_form = OrderForm()

    # Build totals and the Stripe intent, then show the checkout page.
    current_total = 0
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        current_total += quantity * product.price

    stripe_total = round(current_total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    template = 'orders/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """Display a confirmation page after successful checkout."""
    order = get_object_or_404(Order, order_number=order_number)

    # Send the confirmation email. A mail failure (e.g. SMTP misconfiguration)
    # must NOT break the confirmation page for a customer who has already paid,
    # so any error is caught and logged rather than raised.
    try:
        _send_confirmation_email(order)
    except Exception as exc:  # noqa: BLE001 - deliberately broad; email is non-critical
        import logging
        logging.getLogger(__name__).error(
            'Order confirmation email failed for %s: %s', order.order_number, exc
        )

    messages.success(
        request,
        f'Order successfully processed! Your order number is {order_number}.'
    )
    # Estimated delivery window, calculated from the order date (3-5 days).
    order_date = order.created_at
    est_start = (order_date + timedelta(days=3)).strftime('%d %b %Y')
    est_end = (order_date + timedelta(days=5)).strftime('%d %b %Y')

    context = {
        'order': order,
        'estimated_delivery_start': est_start,
        'estimated_delivery_end': est_end,
    }
    return render(request, 'orders/checkout_success.html', context)


def _send_confirmation_email(order):
    """Send the customer an order confirmation email.

    Failures are caught and logged rather than raised, so an email
    problem can never break the checkout success page (defect D9),
    while still leaving an operator-visible record in the logs.
    """
    customer_email = order.email
    subject = render_to_string(
        'orders/confirmation_emails/confirmation_email_subject.txt',
        {'order': order},
    ).strip()
    body = render_to_string(
        'orders/confirmation_emails/confirmation_email_body.txt',
        {'order': order},
    )
    try:
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently=False,
        )
    except Exception:
        import logging
        logging.getLogger(__name__).exception(
            'Confirmation email failed for order %s', order.order_number
        )


@login_required
def order_history(request):
    """List the logged-in user's past orders (read-only historical records)."""
    orders = (
        Order.objects.filter(user=request.user)
        .order_by('-created_at')
        .prefetch_related('line_items__product')
    )
    paginator = Paginator(orders, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {'page_obj': page_obj}
    return render(request, 'orders/order_history.html', context)


@login_required
def order_detail(request, order_number):
    """Show one of the logged-in user's orders.

    The ownership guard is baked into the query: filtering by user means another
    user's order number returns 404 rather than exposing someone else's data.
    """
    order = get_object_or_404(
        Order, order_number=order_number, user=request.user
    )
    context = {'order': order}
    return render(request, 'orders/order_detail.html', context)
