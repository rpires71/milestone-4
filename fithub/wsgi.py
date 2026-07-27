"""
The WSGI (Web Server Gateway Interface) configuration file defines the
application's synchronous entry point. It enables the Django project to
communicate with WSGI-compatible web servers, such as Gunicorn, allowing
HTTP requests to be processed and responses to be returned to users in a
production environment.

For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

# Import Django's WSGI application factory, which creates the callable
# object used by WSGI-compatible web servers to handle incoming HTTP
# requests.
from django.core.wsgi import get_wsgi_application


# Specify the default Django settings module so that the application loads
# the correct project configuration before serving any requests.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fithub.settings')


# Create the WSGI application object. This callable serves as the entry
# point for production web servers, enabling requests to be routed through
# the Django application.
application = get_wsgi_application()
