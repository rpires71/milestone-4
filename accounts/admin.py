"""Admin registrations for the accounts app."""

from django.contrib import admin

from .models import Profile

# Register Profile with the default ModelAdmin. Profiles are created and
# edited by members through the front-end dashboard, so the admin provides
# staff with read/support access rather than a primary editing workflow.
admin.site.register(Profile)
