from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    """A membership plan, mapped to a Stripe Product and Price."""

    TIER_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    INTERVAL_CHOICES = [
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
    ]
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
        ('archived', 'Archived'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    tier = models.CharField(max_length=20, choices=TIER_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    billing_interval = models.CharField(
        max_length=10, choices=INTERVAL_CHOICES, default='monthly'
    )
    image = models.ImageField(upload_to='plans/', null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft'
    )
    stripe_product_id = models.CharField(max_length=255, blank=True)
    stripe_price_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PlanFeature(models.Model):
    """A single 'what's included' line for a plan."""

    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE, related_name='features'
    )
    text = models.CharField(max_length=255)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.plan.name}: {self.text}"


class Subscription(models.Model):
    """A member's subscription to a plan, synced with Stripe."""

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('past_due', 'Past due'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subscriptions'
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT, related_name='subscriptions'
    )
    stripe_subscription_id = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='active'
    )
    current_period_end = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} – {self.plan.name} ({self.status})"
