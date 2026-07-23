"""App configuration for the cart app."""

from django.apps import AppConfig


class CartConfig(AppConfig):
    """Django app configuration for cart."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
