"""App configuration for the accounts app."""

# Every Django app has an AppConfig class. Django uses it to register the
# app and to run any app-specific startup code. AppConfig is the base class
# we inherit from to describe this app to the framework.
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Django app configuration for accounts."""

    # This sets the default type of primary key Django creates for models
    # in this app that don't define one explicitly. BigAutoField is a
    # 64-bit auto-incrementing integer (1, 2, 3, ...), which allows for far
    # more rows than the older 32-bit AutoField. Since Django 3.2 this is
    # the recommended default, which is why it appears in every app.
    default_auto_field = 'django.db.models.BigAutoField'

    # The Python import path of the app. Django uses this name to find the
    # app's models, templates, migrations, etc. It must match the folder
    # name ('accounts') and the entry in INSTALLED_APPS in settings.py.
    name = 'accounts'
