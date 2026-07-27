# The urls.py file defines the URL patterns for the Reviews application.
# Each route connects a browser request to the appropriate review view and
# assigns a reusable name that can be referenced from templates, redirects
# and automated tests.

from django.urls import path

# Import the views responsible for creating, editing and deleting reviews.
from . import views


urlpatterns = [
    # Use the product slug to identify the item that the authenticated user
    # wishes to review.
    path(
        'add/<slug:slug>/',
        views.add_review,
        name='add_review',
    ),

    # Use the review's numeric primary key to identify the existing record
    # that its owner wishes to update.
    path(
        'edit/<int:review_id>/',
        views.edit_review,
        name='edit_review',
    ),

    # Route deletion requests to a confirmation workflow for the selected
    # review record.
    path(
        'delete/<int:review_id>/',
        views.delete_review,
        name='delete_review',
    ),
]
