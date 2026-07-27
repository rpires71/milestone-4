# The views.py file controls the main business logic for the Orders
# application. It receives HTTP requests, processes checkout forms,
# communicates with Stripe, creates orders and line items, updates stock,
# sends confirmation emails and displays customers' previous orders.
#
# These views connect the presentation layer, database models, session cart
# and external payment service. The module therefore includes safeguards
# such as atomic database transactions, authentication checks, ownership
# filtering and payment metadata caching.

"""Views for the checkout flow, order confirmation and order history."""

# Import JSON support so cart and delivery data can be stored within
# Stripe Payment Intent metadata.
import json

# Import UUID generation so every order can receive a unique reference.
import uuid

# Import timedelta to calculate the estimated delivery date range.
from datetime import timedelta

# Import Stripe's Python library for creating and updating Payment Intents.
import stripe

# Import project settings containing Stripe keys, currency and email settings.
from django.conf import settings

# Import Django's message framework for displaying feedback to users.
from django.contrib import messages

# Import login_required to protect personal order-history pages.
from django.contrib.auth.decorators import login_required

# Import Django's email utility for sending order confirmations.
from django.core.mail import send_mail

# Import Paginator so large order histories can be divided into pages.
from django.core.paginator import Paginator

# Import transaction support so related database changes are committed
# together or rolled back together if an error occurs.
from django.db import transaction

# Import HttpResponse for returning status codes to checkout JavaScript.
from django.http import HttpResponse

# Import shortcut functions for retrieving records, redirecting users,
# rendering templates and resolving named URL routes.
from django.shortcuts import get_object_or_404, redirect, render, reverse

# Import render_to_string so email subject and body templates can be
# converted into plain text.
from django.template.loader import render_to_string

# Import require_POST to restrict the metadata-caching endpoint to POST
# requests only.
from django.views.decorators.http import require_POST

# Import Product so checkout totals, order lines and stock levels can be
# calculated from the current catalogue.
from shop.models import Product

# Import the checkout form used to collect and validate delivery details.
from .forms import OrderForm

# Import the models used to create orders and their individual line items.
from .models import Order, OrderLineItem


def checkout(request):
    """
    Display the checkout page and process valid checkout submissions.

    The view retrieves the session cart, calculates the order total,
    creates a Stripe Payment Intent and stores the completed order in the
    database after the delivery form has been validated.
    """

    # Retrieve the publishable Stripe key required by the browser-side
    # checkout JavaScript.
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    # Configure the Stripe library with the secret key used for secure
    # server-side API requests.
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    # Retrieve the current cart from the user's session. An empty dictionary
    # is used when no cart has yet been created.
    cart = request.session.get('cart', {})

    # Prevent users from proceeding to checkout without any products.
    if not cart:
        messages.error(
            request,
            "There's nothing in your basket at the moment"
        )
        return redirect(reverse('products'))

    # Process the submitted checkout form when the browser sends a POST
    # request.
    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        # Continue only when Django's form validation has succeeded.
        if order_form.is_valid():

            # Create the Order object in memory without saving it yet,
            # allowing additional fields to be assigned first.
            order = order_form.save(commit=False)

            # Associate the order with the authenticated user where possible.
            # Guest orders remain valid by storing no user relationship.
            order.user = (
                request.user
                if request.user.is_authenticated
                else None
            )

            # Extract the Payment Intent identifier from Stripe's client
            # secret. Saving this identifier connects the local order with
            # the corresponding Stripe payment and supports idempotency.
            client_secret = request.POST.get('client_secret', '')
            pid = (
                client_secret.split('_secret')[0]
                if client_secret
                else ''
            )
            order.stripe_payment_intent_id = pid

            # Store the cart and delivery details in Stripe metadata. This
            # allows the webhook to reconstruct the order if the customer's
            # browser closes before the normal checkout flow finishes.
            if pid:
                try:
                    stripe.PaymentIntent.modify(
                        pid,
                        metadata={
                            'cart': json.dumps(cart),
                            'full_name': order.full_name,
                            'email': order.email,
                            'phone': order.phone,
                            'address_line1': order.address_line1,
                            'address_line2': order.address_line2,
                            'town_city': order.town_city,
                            'postcode': order.postcode,
                            'country': order.country,
                            'username': (
                                request.user.username
                                if request.user.is_authenticated
                                else ''
                            ),
                        }
                    )

                # A metadata failure should not prevent the normal checkout
                # flow from creating the order. It only reduces the ability
                # of the webhook to rebuild the order as a fallback.
                except Exception:
                    pass

            # Calculate the subtotal directly from database product prices
            # rather than trusting totals supplied by the browser.
            subtotal = 0

            for item_id, quantity in cart.items():
                product = get_object_or_404(Product, pk=item_id)
                subtotal += quantity * product.price

            # Store the financial summary on the order.
            order.subtotal = subtotal
            order.delivery_cost = 0
            order.total = subtotal

            # Generate a unique uppercase order reference.
            order.order_number = uuid.uuid4().hex.upper()

            # Save the order, line items and stock changes within one atomic
            # transaction. If one operation fails, Django rolls back all
            # related database changes to maintain consistency.
            with transaction.atomic():
                order.save()

                # Create one OrderLineItem for each product in the cart.
                for item_id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=item_id)

                    # Snapshot the product price so historical order values
                    # remain unchanged if catalogue prices are updated later.
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price=product.price,
                    )

                    # Reduce stock by the purchased quantity. max() ensures
                    # that the stored value cannot fall below zero.
                    new_stock = max(product.stock - quantity, 0)

                    # Update the stock value directly in the database.
                    Product.objects.filter(
                        pk=product.pk
                    ).update(stock=new_stock)

            # Empty the session cart after the order has been created.
            request.session['cart'] = {}

            # Redirect to the confirmation page using the new order number.
            return redirect(
                reverse(
                    'checkout_success',
                    args=[order.order_number]
                )
            )

        # Inform the user when form validation fails.
        messages.error(
            request,
            'Please correct the highlighted fields below.'
        )

    else:
        # Display a blank checkout form for an initial GET request.
        order_form = OrderForm()

    # Recalculate the current cart total before creating the Stripe
    # Payment Intent.
    current_total = 0

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        current_total += quantity * product.price

    # Stripe expects the amount in the currency's smallest unit, so pounds
    # are converted to pence.
    stripe_total = round(current_total * 100)

    # Create a Stripe Payment Intent representing the amount to be paid.
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Define the checkout template and values required by the page.
    template = 'orders/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Display the confirmation page for a completed order.

    The view retrieves the order, attempts to send a confirmation email and
    calculates an estimated delivery window. Email problems are prevented
    from interrupting access to the confirmation page.
    """

    # Retrieve the completed order or return HTTP 404 if the reference is
    # invalid.
    order = get_object_or_404(
        Order,
        order_number=order_number
    )

    # Attempt to send the order confirmation email. Email delivery is
    # non-critical because the customer's payment and order have already
    # been recorded.
    try:
        _send_confirmation_email(order)

    # Catch unexpected email-related errors so the confirmation page still
    # loads for the customer.
    except Exception as exc:
        # Import logging locally because it is required only for this error
        # path.
        import logging

        logging.getLogger(__name__).error(
            'Order confirmation email failed for %s: %s',
            order.order_number,
            exc
        )

    # Display a success message containing the customer's order reference.
    messages.success(
        request,
        (
            'Order successfully processed! '
            f'Your order number is {order_number}.'
        )
    )

    # Calculate an estimated delivery period of three to five days after
    # the order was created.
    order_date = order.created_at
    est_start = (
        order_date + timedelta(days=3)
    ).strftime('%d %b %Y')
    est_end = (
        order_date + timedelta(days=5)
    ).strftime('%d %b %Y')

    # Pass the order and estimated dates to the confirmation template.
    context = {
        'order': order,
        'estimated_delivery_start': est_start,
        'estimated_delivery_end': est_end,
    }

    return render(
        request,
        'orders/checkout_success.html',
        context
    )


def _send_confirmation_email(order):
    """
    Generate and send an order confirmation email to the customer.

    Email errors are logged rather than raised so a mail-server problem
    cannot break the checkout confirmation page after payment has succeeded.
    """

    # Retrieve the recipient address stored during checkout.
    customer_email = order.email

    # Render the subject from a dedicated template and remove surrounding
    # whitespace or line breaks.
    subject = render_to_string(
        'orders/confirmation_emails/'
        'confirmation_email_subject.txt',
        {'order': order},
    ).strip()

    # Render the email body using the completed order as template context.
    body = render_to_string(
        'orders/confirmation_emails/'
        'confirmation_email_body.txt',
        {'order': order},
    )

    try:
        # Send the confirmation email using the configured sender address.
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently=False,
        )

    # Log the full exception when email delivery fails. The exception is
    # deliberately not re-raised because email is not part of the database
    # transaction or payment completion.
    except Exception:
        import logging

        logging.getLogger(__name__).exception(
            'Confirmation email failed for order %s',
            order.order_number
        )


@login_required
def order_history(request):
    """
    Display a paginated list of orders belonging to the logged-in user.

    Authentication is required because order records contain personal,
    delivery and purchasing information.
    """

    # Retrieve only orders owned by the current user and display the newest
    # orders first.
    orders = (
        Order.objects
        .filter(user=request.user)
        .order_by('-created_at')

        # Load related line items and products efficiently to reduce the
        # number of separate database queries required by the template.
        .prefetch_related('line_items__product')
    )

    # Divide the order history into pages containing ten orders each.
    paginator = Paginator(orders, 10)

    # Retrieve the requested page number. get_page() handles missing or
    # invalid page values safely.
    page_obj = paginator.get_page(
        request.GET.get('page')
    )

    context = {
        'page_obj': page_obj
    }

    return render(
        request,
        'orders/order_history.html',
        context
    )


@login_required
def order_detail(request, order_number):
    """
    Display one order belonging to the logged-in user.

    Including the current user in the database query acts as an ownership
    guard. A user attempting to access another customer's order receives
    HTTP 404 rather than being shown private information.
    """

    # Retrieve the order only when both its number and owner match.
    order = get_object_or_404(
        Order,
        order_number=order_number,
        user=request.user
    )

    context = {
        'order': order
    }

    return render(
        request,
        'orders/order_detail.html',
        context
    )


@require_POST
def cache_checkout_data(request):
    """
    Attach cart and customer details to the Stripe Payment Intent before
    card payment is confirmed.

    The checkout JavaScript calls this endpoint immediately before Stripe
    processes the payment. The metadata enables the webhook to rebuild the
    order if the browser closes or loses connection before returning to the
    application.
    """

    try:
        # Extract the Payment Intent identifier from the submitted client
        # secret.
        pid = request.POST.get(
            'client_secret',
            ''
        ).split('_secret')[0]

        # Configure Stripe for the server-side metadata update.
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Retrieve the current cart from the user's session.
        cart = request.session.get('cart', {})

        # Attach cart, delivery and account details to the Payment Intent.
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                'cart': json.dumps(cart),
                'full_name': request.POST.get('full_name', ''),
                'email': request.POST.get('email', ''),
                'phone': request.POST.get('phone', ''),
                'address_line1': request.POST.get(
                    'address_line1',
                    ''
                ),
                'address_line2': request.POST.get(
                    'address_line2',
                    ''
                ),
                'town_city': request.POST.get('town_city', ''),
                'postcode': request.POST.get('postcode', ''),
                'country': request.POST.get('country', ''),
                'username': (
                    request.user.username
                    if request.user.is_authenticated
                    else ''
                ),
            }
        )

        # Return HTTP 200 so the checkout JavaScript can continue to payment.
        return HttpResponse(status=200)

    # A broad exception is used because failures may originate from Stripe,
    # configuration, networking or malformed request data.
    # pylint: disable=broad-exception-caught
    except Exception as error:
        # Display a user-friendly message while returning the technical
        # error to the JavaScript request.
        messages.error(
            request,
            (
                'Sorry, your payment cannot be processed right now. '
                'Please try again later.'
            )
        )

        return HttpResponse(
            content=str(error),
            status=400
        )
