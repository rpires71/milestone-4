"""URL routes for the accounts app."""

# path() is the function that maps a URL pattern to a view. It's the core
# building block of Django's URL routing.
from django.urls import path

# Import this app's views module. "from . import views" means "from the current
# package (accounts), import views" — so views.dashboard refers to the dashboard
# function in accounts/views.py.
from . import views

# urlpatterns is a list Django looks for BY NAME — it must be called exactly this.
# Django checks each pattern top-to-bottom and uses the FIRST one that matches
# the incoming URL.
urlpatterns = [
    # path(route, view, name) has three parts:
    #   route: the URL pattern to match (relative to where this file is included)
    #   view:  the function to run when it matches
    #   name:  a label used to refer to this URL elsewhere, so you never hardcode
    #          the actual path string
    #
    # '' = the empty route = the app's root. Since this file is included under
    # /accounts/ in the project urls, '' here means the URL /accounts/ itself,
    # which runs the dashboard view.
    path('', views.dashboard, name='dashboard'),

    # Matches /accounts/profile-setup/ and runs the profile_setup view.
    path('profile-setup/', views.profile_setup, name='profile_setup'),

    # Matches /accounts/profile/edit/ and runs the profile_edit view. Slashes
    # within the route create the URL structure.
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
