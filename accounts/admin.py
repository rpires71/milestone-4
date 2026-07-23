"""Admin registrations for the accounts app."""

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
