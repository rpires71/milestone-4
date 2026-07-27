# The admin.py file configures how the Orders application's models are
# presented within the Django administration site. Registering models
# enables authorised administrators to create, view, update and manage
# order data through Django's secure web-based administration interface.
# The file also provides a location for customising the administrative
# interface with features such as list displays, search fields, filters
# and ordering where required.

"""Admin registrations for orders and line items."""

from django.contrib import admin

# Import the models that should be available through the Django
# administration interface.
from .models import Order, OrderLineItem


# Register the Order model so that administrators can manage customer
# orders using the Django administration site.
admin.site.register(Order)

# Register the OrderLineItem model so that administrators can view and
# manage the individual products associated with each order.
admin.site.register(OrderLineItem)
