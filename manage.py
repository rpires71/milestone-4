#!/usr/bin/env python

# The manage.py file provides a command-line interface for interacting with
# the Django application. It allows developers to execute administrative
# tasks such as starting the development server, creating database migrations,
# applying migrations, running automated tests and managing application data.

"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """
    Configure the Django settings module and execute the requested
    management command supplied through the command line.
    """

    # Set the default Django settings module so that Django knows which
    # project configuration to load before executing any management command.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fithub.settings')

    try:
        # Import Django's command-line execution utility, which processes
        # management commands such as runserver, migrate and test.
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        # Raise a clear error message if Django cannot be imported. This
        # commonly occurs when dependencies have not been installed or the
        # project's virtual environment has not been activated.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the management command supplied by the user, together with
    # any additional command-line arguments.
    execute_from_command_line(sys.argv)


# Ensure that the main() function is executed only when this file is run
# directly, preventing it from running automatically if imported elsewhere.
if __name__ == '__main__':
    main()
