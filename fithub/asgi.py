"""
The ASGI (Asynchronous Server Gateway Interface) configuration file defines
the application's asynchronous entry point. It enables the Django project to
communicate with ASGI-compatible web servers and supports asynchronous
features such as WebSockets, long-running connections and asynchronous
request handling.

For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

# Import Django's ASGI application factory, which creates the callable
# object used by ASGI-compatible servers to process incoming requests.
from django.core.asgi import get_asgi_application


# Specify the default Django settings module so that the application loads
# the correct project configuration before handling any requests.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fithub.settings')


# Create the ASGI application object. This callable acts as the entry point
# for asynchronous web servers, allowing requests to be routed through the
# Django application.
application = get_asgi_application()
