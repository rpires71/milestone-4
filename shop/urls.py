# The urls.py file defines the URL patterns for the Shop application.
# Each route maps an incoming HTTP request to the appropriate view,
# allowing customers to browse the product catalogue and view individual
# product details. Named URLs also provide a consistent way to generate
# links throughout templates, views and automated tests.

from django.urls import path

# Import the views responsible for displaying the product catalogue and
# individual product pages.
from . import views


urlpatterns = [
    # Display the main product catalogue containing all products that are
    # currently available for purchase.
    path(
        '',
        views.all_products,
        name='products',
    ),

    # Display the detail page for a specific product identified by its
    # unique URL slug.
    path(
        '<slug:slug>/',
        views.product_detail,
        name='product_detail',
    ),
]
