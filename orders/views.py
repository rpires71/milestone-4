from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


import stripe
import uuid

from shop.models import Product
from .models import Order, OrderLineItem
from .forms import OrderForm


def checkout(request):
    """Handle the checkout process and Stripe payment."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None

            subtotal = 0
            for item_id, quantity in cart.items():
                product = get_object_or_404(Product, pk=item_id)
                subtotal += quantity * product.price

            order.subtotal = subtotal
            order.delivery_cost = 0
            order.total = subtotal
            order.order_number = uuid.uuid4().hex.upper()
            order.save()

            # Create a line item for each product in the cart
            for item_id, quantity in cart.items():
                product = get_object_or_404(Product, pk=item_id)
                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price,
                )

            # Clear the cart and go to success page
            request.session['cart'] = {}
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please check your details.')

    # GET request — build totals and show the checkout page
    current_total = 0
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        current_total += quantity * product.price

    stripe_total = round(current_total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
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

    # Send the confirmation email
    _send_confirmation_email(order)

    messages.success(
        request,
        f'Order successfully processed! Your order number is {order_number}.'
    )
    context = {'order': order}
    return render(request, 'orders/checkout_success.html', context)


def _send_confirmation_email(order):
    """Send the customer an order confirmation email."""
    customer_email = order.email
    subject = render_to_string(
        'orders/confirmation_emails/confirmation_email_subject.txt',
        {'order': order},
    ).strip()
    body = render_to_string(
        'orders/confirmation_emails/confirmation_email_body.txt',
        {'order': order},
    )
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email],
        fail_silently=False,
    )


