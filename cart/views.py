"""Views for adding, updating and removing basket items."""

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
# format_html safely builds HTML strings with placeholders — it escapes the
# inserted values so they can't inject malicious markup. This replaced an
# unsafe mark_safe() call (defect D22).
from django.utils.html import format_html
from django.views.decorators.http import require_POST

from shop.models import Product


def view_cart(request):
    """Display the current shopping cart."""
    # The simplest view: just render the template. It needs no context here
    # because the cart_contents context processor already injects cart_items,
    # total, and product_count into EVERY template automatically.
    return render(request, 'cart/cart.html')


@require_POST
def add_to_cart(request, product_id):
    """Add a quantity of a product to the cart, capped at available stock."""
    # product_id was captured from the URL (<int:product_id>). Look up the real
    # product, or 404 if the id doesn't exist.
    product = get_object_or_404(Product, pk=product_id)
    # Where to send the user afterward. The form passes redirect_url (e.g. the
    # product page they added from); fall back to the cart page if absent.
    redirect_url = request.POST.get('redirect_url') or 'view_cart'

    # DEFENSIVE INPUT PARSING. request.POST values are strings. int() might fail
    # if someone sends 'abc' — the try/except catches that and defaults to 1
    # instead of crashing. (This is what test_add_with_non_numeric... verifies.)
    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        quantity = 1
    # Guard against negative numbers — clamp anything below 1 up to 1.
    # (test_add_with_negative_quantity... verifies this.)
    if quantity < 1:
        quantity = max(quantity, 1)

    # Read the current basket from the session (empty dict if none yet).
    cart = request.session.get('cart', {})
    # How many of this product are ALREADY in the basket (0 if none).
    current = cart.get(str(product_id), 0)
    # The total they'd have after this add.
    requested = current + quantity

    # STOCK CAPPING (defect D5). You can't add more than exists.
    if requested > product.stock:
        # Cap the basket quantity at the available stock.
        cart[str(product_id)] = product.stock
        if product.stock == 0:
            # Nothing in stock at all: remove it entirely and warn.
            # pop(key, None) removes safely — the None default means it won't
            # error if the key isn't there.
            cart.pop(str(product_id), None)
            messages.warning(request, f'Sorry, {product.name} is out of stock.')
        else:
            # Some stock, but less than requested: cap and explain.
            messages.warning(
                request,
                f'Only {product.stock} of {product.name} in stock — '
                f'quantity set to {product.stock}.'
            )
    else:
        # Enough stock: set the new quantity.
        cart[str(product_id)] = requested
        basket_url = reverse('view_cart')
        # format_html builds a success message WITH a clickable "View basket"
        # link. The {} placeholders are filled by the arguments below, and
        # format_html ESCAPES product.name (so a product named "<script>" can't
        # inject anything). This is the D22 fix — safe HTML in a flash message.
        messages.success(request, format_html(
            'Added {} to your basket. '
            '<a href="{}" class="alert-link">View basket</a>',
            product.name,
            basket_url,
        ))

    # WRITE THE BASKET BACK to the session. This line is essential — modifying
    # the local `cart` dict doesn't persist until you reassign it to the session.
    request.session['cart'] = cart
    # Redirect (PRG pattern) so a refresh doesn't re-add the item.
    return redirect(redirect_url)


@require_POST
def adjust_cart(request, product_id):
    """Set the quantity of a product in the cart, capped at available stock."""
    product = get_object_or_404(Product, pk=product_id)

    # Note the difference from add: adjust defaults to 0, not 1. That's because
    # adjust SETS the quantity, and a bad/empty value should mean "remove"
    # rather than "add one". (test_adjust_with_non_numeric... verifies removal.)
    try:
        quantity = int(request.POST.get('quantity', 0))
    except (TypeError, ValueError):
        quantity = 0

    cart = request.session.get('cart', {})

    # Three branches: remove / cap / set.
    if quantity <= 0:
        # Zero or negative = remove the item. (D5-adjacent; matches the tests
        # for adjust-to-zero and negative-adjust removal.)
        cart.pop(str(product_id), None)
        messages.success(request, f'Removed {product.name} from your basket.')
    elif quantity > product.stock:
        # More than available: cap at stock.
        cart[str(product_id)] = product.stock
        messages.warning(
            request,
            f'Only {product.stock} of {product.name} in stock — '
            f'quantity set to {product.stock}.'
        )
    else:
        # Valid quantity within stock: set it exactly.
        cart[str(product_id)] = quantity
        messages.success(request, f'Updated {product.name} quantity to {quantity}.')

    request.session['cart'] = cart
    return redirect('view_cart')


@require_POST
def remove_from_cart(request, product_id):
    """Remove a product from the cart entirely."""
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    # pop(key, None) removes the item if present, does nothing if not — no crash
    # either way. The simplest of the three write operations.
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    messages.success(request, f'Removed {product.name} from your basket.')
    return redirect('view_cart')
