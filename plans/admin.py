# The admin.py file configures how the Plans application's models are
# presented within Django's administration site. Registering models and
# customising their administration interface enables authorised users to
# manage subscription plans, plan features and customer subscriptions
# through Django's secure web-based administration system.

from django.contrib import admin

# Import the models that will be managed through the Django
# administration interface.
from .models import Plan, PlanFeature, Subscription


class PlanFeatureInline(admin.TabularInline):
    """
    Display PlanFeature records within the Plan editing page.

    Using an inline allows administrators to create, edit and remove
    plan features without leaving the parent plan form, improving both
    efficiency and usability.
    """

    # Specify the related model displayed inline.
    model = PlanFeature

    # Display three empty rows by default to encourage administrators to
    # add multiple plan features when creating a new subscription plan.
    extra = 3


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    """
    Customise the administration interface for subscription plans.
    """

    # Display the most important plan information in the list view so
    # administrators can quickly compare available plans.
    list_display = (
        'name',
        'tier',
        'price',
        'billing_interval',
        'status',
    )

    # Provide filters that make locating plans easier as the number of
    # available plans increases.
    list_filter = (
        'tier',
        'billing_interval',
        'status',
    )

    # Enable keyword searches using the plan name and description.
    search_fields = (
        'name',
        'description',
    )

    # Automatically generate the URL slug from the plan name to reduce
    # manual data entry and maintain consistent URLs.
    prepopulated_fields = {
        'slug': ('name',)
    }

    # Display related plan features directly on the plan editing page.
    inlines = [PlanFeatureInline]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Customise the administration interface for customer subscriptions.
    """

    # Display key subscription information to help administrators monitor
    # customer accounts and subscription status.
    list_display = (
        'user',
        'plan',
        'status',
        'current_period_end',
    )

    # Allow subscriptions to be filtered according to their current
    # lifecycle status.
    list_filter = (
        'status',
    )
