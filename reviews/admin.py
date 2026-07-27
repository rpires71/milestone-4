# The admin.py file registers the Review model with Django's
# administration site, allowing authorised administrators to create,
# view, edit and remove customer reviews through Django's secure
# web-based administration interface.

from django.contrib import admin

# Import the model that will be managed through the administration site.
from .models import Review


# Register the Review model using Django's default administration
# interface. This provides standard CRUD functionality without requiring
# additional customisation.
admin.site.register(Review)
