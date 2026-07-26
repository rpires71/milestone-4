"""Context processor exposing basket contents to all templates."""

# Decimal is used for money instead of float. Floats have rounding errors
# (0.1 + 0.2 != 0.3 in float), which is unacceptable for prices. Decimal is
# exact — the correct type for any monetary calculation.
from decimal import Decimal

# get_object_or_404 fetches an object or raises a 404 if it doesn't exist,
# rather than crashing with an error.
from django.shortcuts import get_object_or_404

from shop.models import Product


# THIS IS A CONTEXT PROCESSOR — a function that runs on EVERY request and
# injects its return value into the context of EVERY template automatically.
# It's registered in settings.py under TEMPLATES > OPTIONS > context_processors.
# That registration is what makes cart_items, total, and product_count available
# in every template WITHOUT any view having to pass them.
def cart_contents(request):
    """Make the cart contents available across all templates."""
    # Start with empty accumulators. We'll build these up by walking the cart.
    cart_items = []
    total = Decimal(0)          # Decimal(0), not 0, to keep money arithmetic exact
    product_count = 0

    # THE SESSION IS THE BASKET. request.session is a per-browser dictionary
    # Django persists automatically. .get('cart', {}) reads the 'cart' key, or
    # returns an empty dict {} if nothing's been added yet (so this never crashes
    # on a first-time visitor). The cart looks like {'3': 2, '7': 1} —
    # {product_id: quantity}.
    cart = request.session.get('cart', {})

    # Walk each entry: item_id is the product's id (as a string, since session
    # keys are strings), quantity is how many.
    for item_id, quantity in cart.items():
        # The session only stores ids + quantities — NOT product details. So we
        # look up the real Product from the database to get its price and name.
        # This is the trade-off of session storage: cheap to store, but you
        # re-fetch product data each request.
        product = get_object_or_404(Product, pk=item_id)
        # Accumulate the running total and item count.
        total += quantity * product.price
        product_count += quantity
        # Build a dictionary for this line and add it to the list. This is the
        # shape the cart.html template loops over: item.product, item.quantity,
        # item.subtotal all come from here.
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': quantity * product.price,
        })

    # Return the three values. Because this is a context processor, these keys
    # become template variables EVERYWHERE — {{ product_count }} in the navbar,
    # {{ cart_items }} and {{ total }} in cart.html, all without a single view
    # passing them explicitly.
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }
    return context
