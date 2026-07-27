# The urls.py file defines the URL patterns for the Plans application.
# Each route connects a browser request to the appropriate view while
# assigning a reusable name that can be referenced safely from templates,
# redirects and automated tests.

from django.urls import path

# Import the Plans views that handle public plan pages, Stripe
# subscriptions and staff-only plan management.
from . import views


urlpatterns = [
    # Display the public list of published membership plans.
    path(
        '',
        views.all_plans,
        name='plans',
    ),

    # Provide staff with an overview of published, draft and archived
    # plans through the custom management interface.
    path(
        'manage/',
        views.manage_plans,
        name='manage_plans',
    ),

    # Allow authorised staff to create a new membership plan.
    path(
        'manage/new/',
        views.plan_create,
        name='plan_create',
    ),

    # Use the plan slug to identify the existing record that staff wish
    # to edit.
    path(
        'manage/<slug:slug>/edit/',
        views.plan_edit,
        name='plan_edit',
    ),

    # Present the archive workflow for a specific plan. Archiving retains
    # the database record instead of permanently deleting it.
    path(
        'manage/<slug:slug>/archive/',
        views.plan_archive,
        name='plan_archive',
    ),

    # Start Stripe Checkout for the published plan identified by its
    # human-readable slug.
    path(
        'subscribe/<slug:slug>/',
        views.subscribe,
        name='subscribe',
    ),

    # Process the user's return from Stripe after subscription checkout.
    path(
        'subscription/success/',
        views.subscription_success,
        name='subscription_success',
    ),

    # Display the public detail page for an individual published plan.
    # This dynamic route is placed last so that fixed paths such as
    # "manage/" and "subscription/success/" are matched first.
    path(
        '<slug:slug>/',
        views.plan_detail,
        name='plan_detail',
    ),
]
