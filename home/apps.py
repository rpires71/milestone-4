# The apps.py file defines the configuration for the Home application.
# Django uses the AppConfig class to register the application, identify
# its configuration settings and perform application-specific
# initialisation when the project starts.

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configure the Home application and provide metadata used by Django
    during application initialisation.
    """

    # Specify the default type of primary key that Django should use when
    # automatically creating model identifiers within this application.
    default_auto_field = 'django.db.models.BigAutoField'

    # Define the application's unique name, allowing Django to identify
    # and register the Home application within the project.
    name = 'home'