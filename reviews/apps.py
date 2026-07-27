# The apps.py file defines the configuration for the Reviews application.
# Django uses the AppConfig class to register the application, identify
# its configuration settings and perform any application-specific
# initialisation required when the project starts.

from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    Configure the Reviews application and provide metadata used by Django
    during application initialisation.
    """

    # Specify the default type of primary key that Django should use when
    # automatically creating model identifiers within this application.
    default_auto_field = 'django.db.models.BigAutoField'

    # Define the application's unique name so that Django can correctly
    # identify and register the Reviews application within the project.
    name = 'reviews'
