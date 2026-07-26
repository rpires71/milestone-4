"""App configuration for the cart app."""

from django.apps import AppConfig


class CartConfig(AppConfig):
    """Django app configuration for cart."""
    # 64-bit auto-incrementing primary key default (Django 3.2+ recommendation).
    # Note: the cart app has no models, so this default is never actually used
    # here â€” it's just the standard boilerplate every app gets.
    default_auto_field = 'django.db.models.BigAutoField'
    # The app's import path; must match the folder name and INSTALLED_APPS entry.
    name = 'cart'
