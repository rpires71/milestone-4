# The models.py file defines the core database structure for the Plans
# application. These models represent membership plans, their individual
# features and customer subscriptions. Together they provide the data
# required to manage subscription products within FitHub while
# maintaining synchronisation with Stripe's payment platform.

from django.contrib.auth.models import User
from django.db import models


class Plan(models.Model):
    """
    Represent a membership plan that can be purchased by users.

    Each plan stores the information required for display within the
    application and maintains references to the corresponding Stripe
    Product and Price, allowing payments and subscriptions to remain
    synchronised between the application and Stripe.
    """

    # Define the available membership tiers presented throughout the
    # application.
    TIER_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    # Restrict billing to the supported subscription intervals.
    INTERVAL_CHOICES = [
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
    ]

    # Control whether a plan is visible and available for purchase.
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
        ('archived', 'Archived'),
    ]

    # Store the plan's public name.
    name = models.CharField(max_length=100)

    # Generate a unique, human-readable identifier for URLs.
    slug = models.SlugField(unique=True)

    # Describe the benefits of the membership plan.
    description = models.TextField(blank=True)

    # Categorise the plan according to its intended experience level.
    tier = models.CharField(max_length=20, choices=TIER_CHOICES)

    # Store the subscription price charged to members.
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Record whether the subscription renews monthly or annually.
    billing_interval = models.CharField(
        max_length=10,
        choices=INTERVAL_CHOICES,
        default='monthly',
    )

    # Optionally associate an image with the membership plan.
    image = models.ImageField(upload_to='plans/', null=True, blank=True)

    # Record whether the plan is available for purchase.
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )

    # Store Stripe's Product identifier to link the application with the
    # corresponding product held by Stripe.
    stripe_product_id = models.CharField(max_length=255, blank=True)

    # Store Stripe's Price identifier used during subscription checkout.
    stripe_price_id = models.CharField(max_length=255, blank=True)

    # Record when the plan was first created.
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically record the date and time of the most recent update.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return the plan name when the object is displayed in the Django
        administration site or interactive shell.
        """
        return self.name


class PlanFeature(models.Model):
    """
    Represent an individual feature included within a membership plan.

    Separating features into their own model provides greater
    flexibility than storing them as plain text, allowing them to be
    ordered, edited and displayed independently.
    """

    # Associate each feature with its parent membership plan. Deleting a
    # plan automatically removes its associated features.
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name='features',
    )

    # Store the description of the individual feature.
    text = models.CharField(max_length=255)

    # Control the order in which features are presented to users.
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        """
        Configure default behaviour for the PlanFeature model.
        """

        # Always display features in the configured display order.
        ordering = ['display_order']

    def __str__(self):
        """
        Return a descriptive representation of the feature.
        """
        return f"{self.plan.name}: {self.text}"


class Subscription(models.Model):
    """
    Represent a member's active or historical subscription.

    Each subscription links a user to a membership plan and stores the
    Stripe subscription identifier so that subscription events can be
    synchronised between FitHub and Stripe.
    """

    # Restrict subscriptions to recognised lifecycle states.
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('past_due', 'Past due'),
    ]

    # Associate the subscription with the authenticated member.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )

    # Associate the subscription with the purchased membership plan.
    # PROTECT prevents plans from being deleted while subscriptions still
    # reference them, preserving historical payment records.
    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        related_name='subscriptions',
    )

    # Store Stripe's subscription identifier for synchronisation with the
    # external payment platform.
    stripe_subscription_id = models.CharField(max_length=255, blank=True)

    # Record the current lifecycle status of the subscription.
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
    )

    # Record when the current billing period expires.
    current_period_end = models.DateTimeField(null=True, blank=True)

    # Automatically record when the subscription was first created.
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically record the most recent modification.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a readable summary of the subscription for use throughout
        the Django administration interface.
        """
        return f"{self.user.username} – {self.plan.name} ({self.status})"
