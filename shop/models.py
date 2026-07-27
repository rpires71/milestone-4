# The models.py file defines the database structure for the Shop
# application. It stores product categories and individual products,
# providing the data required to display the catalogue, manage stock,
# organise merchandise and support the purchasing process throughout
# the FitHub application.

from django.db import models


class ProductCategory(models.Model):
    """
    Represent a category used to organise related products.

    Categories improve navigation by grouping similar products together,
    making it easier for customers to browse the shop and for
    administrators to manage the product catalogue.
    """

    # Store the display name of the product category.
    name = models.CharField(max_length=100)

    # Store a unique, URL-friendly identifier used in category links.
    slug = models.SlugField(unique=True)

    class Meta:
        """
        Configure additional metadata for the ProductCategory model.
        """

        # Use a more natural plural name within the Django administration
        # interface.
        verbose_name_plural = 'Product categories'

    def __str__(self):
        """
        Return the category name as its human-readable representation.

        This improves readability throughout the Django administration
        interface, shell and debugging output.
        """
        return self.name


class Product(models.Model):
    """
    Represent an individual product available for purchase.

    Each product stores descriptive, pricing and inventory information
    required to display products within the shop and support the checkout
    process.
    """

    # Associate the product with an optional category. If a category is
    # deleted, the product remains in the catalogue with no assigned
    # category rather than being removed.
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
    )

    # Store the product's display name.
    name = models.CharField(max_length=200)

    # Store a unique URL-friendly identifier used when generating product
    # detail page URLs.
    slug = models.SlugField(unique=True)

    # Store the product description displayed to customers.
    description = models.TextField()

    # Record the product manufacturer or brand where applicable.
    brand = models.CharField(
        max_length=100,
        blank=True,
    )

    # Store the product's selling price using a fixed decimal format to
    # maintain financial accuracy.
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    # Record the number of items currently available for sale.
    stock = models.PositiveIntegerField(default=0)

    # Store an optional product image uploaded to the media directory.
    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
    )

    # Indicate whether the product is currently available for purchase
    # without needing to remove it from the catalogue.
    is_available = models.BooleanField(default=True)

    # Automatically record when the product was first created.
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically record when the product was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return the product name as its human-readable representation.

        This provides meaningful labels throughout the Django
        administration interface and during development.
        """
        return self.name
