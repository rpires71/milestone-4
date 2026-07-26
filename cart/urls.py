"""URL routes for the cart app."""

from django.urls import path

from . import views

urlpatterns = [
    # '' = the cart app's root. Since this file is included under /cart/ in the
    # project urls, this matches /cart/ itself and shows the basket page.
    path('', views.view_cart, name='view_cart'),

    # <int:product_id> is a URL CONVERTER â€” it CAPTURES part of the URL and
    # passes it to the view as an argument.
    #   int:       only matches integers (so /add/abc/ won't match this route)
    #   product_id the captured number is handed to the view as a keyword arg
    # So /cart/add/7/ calls add_to_cart(request, product_id=7).
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # Same pattern: capture the product id and pass it to adjust_cart.
    # /cart/adjust/7/ -> adjust_cart(request, product_id=7)
    path('adjust/<int:product_id>/', views.adjust_cart, name='adjust_cart'),

    # And remove. /cart/remove/7/ -> remove_from_cart(request, product_id=7)
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
