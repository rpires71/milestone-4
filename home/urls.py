# The urls.py file defines the URL routing for the Home application.
# It maps incoming HTTP requests to the appropriate view functions,
# enabling users to navigate between the application's public pages.
# Separating URL configuration into individual applications promotes a
# modular architecture and improves the maintainability of the project.

from django.urls import path
from . import views


urlpatterns = [

    # Route the root URL of the Home application to the homepage.
    path('', views.index, name='home'),

    # Route requests for the Terms and Conditions page.
    path('terms/', views.terms, name='terms'),

    # Route requests for the Privacy Policy page.
    path('privacy/', views.privacy, name='privacy'),
]
