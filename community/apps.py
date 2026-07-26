"""App configuration for the community app."""

from django.apps import AppConfig


class CommunityConfig(AppConfig):
    """Django app configuration for community."""
    # 64-bit auto-incrementing primary key default (Django 3.2+ standard).
    default_auto_field = 'django.db.models.BigAutoField'
    # The app's import path; matches the folder name and INSTALLED_APPS entry.
    name = 'community'
