# The urls.py file defines the project's URL routing configuration. It maps
# incoming HTTP requests to the appropriate application, providing a single
# entry point that directs users to the correct functionality throughout the
# FitHub website.

from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # Route requests beginning with /admin/ to Django's built-in
    # administration interface, allowing authorised users to manage
    # application data securely.
    path('admin/', admin.site.urls),

    # Include Django Allauth authentication routes, providing features such
    # as registration, login, logout, password reset and account management.
    path('accounts/', include('allauth.urls')),

    # Route all product catalogue requests to the Shop application.
    path('products/', include('shop.urls')),

    # Route subscription plan requests to the Plans application.
    path('plans/', include('plans.urls')),

    # Route product review functionality to the Reviews application.
    path('reviews/', include('reviews.urls')),

    # Route shopping cart functionality to the Cart application.
    path('cart/', include('cart.urls')),

    # Route checkout and order management functionality to the Orders
    # application.
    path('orders/', include('orders.urls')),

    # Route community-related features, such as discussion content,
    # to the Community application.
    path('community/', include('community.urls')),

    # Route user dashboard and profile management requests to the
    # Accounts application.
    path('dashboard/', include('accounts.urls')),

    # Route the site's homepage and other root-level pages to the
    # Home application.
    path('', include('home.urls')),
]
