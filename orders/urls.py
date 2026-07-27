# The urls.py file defines the URL routes used by the Orders application.
# Each route connects a browser request to the appropriate view or webhook
# function. Using named URL patterns allows templates, tests and views to
# reference routes with Django's reverse-resolution system instead of
# relying on hard-coded paths.

"""URL routes for the orders app."""

# Import Django's path function for defining URL patterns.
from django.urls import path

# Import the standard views and Stripe webhook handler used by the
# Orders application.
from . import views, webhooks


# Store all URL routes belonging to the Orders application.
urlpatterns = [
    # Display and process the checkout page. The same view handles both
    # GET requests for displaying the form and POST requests for submitting
    # customer delivery details.
    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    # Display the order confirmation page after checkout. The order number
    # is captured from the URL and used to retrieve the completed order.
    path(
        'checkout/success/<order_number>/',
        views.checkout_success,
        name='checkout_success'
    ),

    # Receive server-to-server Stripe webhook notifications. This endpoint
    # allows the application to verify payment events and reconstruct or
    # confirm orders independently of the customer's browser session.
    path(
        'wh/',
        webhooks.stripe_webhook,
        name='stripe_webhook'
    ),

    # Display the authenticated user's previous orders.
    path(
        'history/',
        views.order_history,
        name='order_history'
    ),

    # Display the details of one order belonging to the authenticated user.
    # The order number is included as a dynamic URL parameter.
    path(
        'history/<order_number>/',
        views.order_detail,
        name='order_detail'
    ),

    # Receive checkout data from the browser and store it in the Stripe
    # Payment Intent metadata before payment confirmation.
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),
]
