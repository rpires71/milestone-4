# The admin.py file customises how the Shop application's models are
# presented within Django's administration interface. The configuration
# improves data management by controlling which fields are displayed,
# enabling filtering and searching, and automatically generating URL
# slugs from product and category names.

from django.contrib import admin

# Import the models that will be managed through the administration site.
from .models import Product, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """
    Configure the administration interface for product categories.

    The customisation makes category records easier to manage by
    displaying key information and automatically generating URL-friendly
    slugs from category names.
    """

    # Display the category name and slug within the administration list
    # view so administrators can quickly identify each record.
    list_display = (
        'name',
        'slug',
    )

    # Automatically populate the slug field as the category name is
    # entered, helping to maintain consistent and readable URLs.
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Configure the administration interface for shop products.

    The customisation improves usability by displaying important product
    information, providing filtering and search functionality, and
    automatically generating product slugs.
    """

    # Display the most important product information in the list view,
    # allowing administrators to monitor inventory efficiently.
    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'is_available',
    )

    # Provide filters that allow administrators to quickly locate
    # products by category or availability status.
    list_filter = (
        'category',
        'is_available',
    )

    # Enable keyword searching across commonly used descriptive fields,
    # making products easier to locate within large catalogues.
    search_fields = (
        'name',
        'brand',
        'description',
    )

    # Automatically generate a URL-friendly slug from the product name,
    # reducing manual data entry and ensuring consistency.
    prepopulated_fields = {
        'slug': ('name',),
    }
