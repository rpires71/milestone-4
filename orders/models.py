# The models.py file defines the database structure for the Orders
# application. Each Django model represents a database table, allowing
# Django's Object-Relational Mapper (ORM) to manage customer orders and
# their associated products without requiring raw SQL queries. These
# models store completed purchases, delivery information and the
# individual products contained within each order.

"""Models for orders and their line items."""

# Import Django's built-in User model so that completed orders can be
# associated with registered customers.
from django.contrib.auth.models import User

# Import Django's model framework, which provides the classes required
# to define database tables and their relationships.
from django.db import models

# Import the Product model so that each order line item can reference
# an existing product in the shop catalogue.
from shop.models import Product


class Order(models.Model):
    """
    Represent a completed customer order created after successful
    payment confirmation. The model stores customer details, delivery
    information, payment references and order totals.
    """

    # Define the available stages in the order fulfilment process,
    # allowing administrators to track the progress of each order.
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('dispatched', 'Dispatched'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]

    # Store a unique reference number used to identify each order.
    order_number = models.CharField(
        max_length=32,
        unique=True,
        editable=False
    )

    # Associate the order with a registered user where applicable.
    # The relationship is optional so that guest checkouts remain
    # possible, and the order is preserved if the user account is deleted.
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    # Store the customer's delivery details.
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120, blank=True)
    town_city = models.CharField(max_length=60)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=60)

    # Store the financial summary of the order.
    subtotal = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # Record the current fulfilment status of the order.
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='processing'
    )

    # Store the Stripe Payment Intent identifier so that payments can
    # be reconciled with Stripe webhooks.
    stripe_payment_intent_id = models.CharField(
        max_length=255,
        blank=True
    )

    # Automatically record when the order was created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return the order number as the human-readable representation of
        the model within Django's administration interface.
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    Represent an individual product purchased as part of an order.
    Each line item stores the quantity purchased together with a
    snapshot of the product price at the time of purchase.
    """

    # Associate the line item with its parent order. Deleting an order
    # automatically removes its associated line items.
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='line_items'
    )

    # Associate the line item with a product. PROTECT prevents products
    # from being deleted if they are referenced by existing orders,
    # preserving historical order records.
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    # Store the quantity of the selected product purchased.
    quantity = models.PositiveIntegerField(default=1)

    # Store the product price at the time of purchase so that historical
    # orders remain accurate even if catalogue prices change later.
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        """
        Return a descriptive representation of the order line item,
        including the quantity, product name and associated order.
        """
        return (
            f"{self.quantity} x {self.product.name} "
            f"(Order {self.order.order_number})"
        )
