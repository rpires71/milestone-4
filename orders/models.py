from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Order(models.Model):
    """A completed one-time purchase, confirmed via Stripe webhook."""

    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('dispatched', 'Dispatched'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]

    order_number = models.CharField(max_length=32, unique=True, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders'
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120, blank=True)
    town_city = models.CharField(max_length=60)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=60)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='processing'
    )
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """A single product line within an order (price snapshotted)."""

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='line_items'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.order_number})"