from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.utils.safestring import mark_safe
from shop.models import Product


def view_cart(request):
    """Display the current shopping cart."""
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """Add a quantity of a product to the cart, capped at available stock."""
    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.POST.get('redirect_url') or 'view_cart'

    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        quantity = 1
    if quantity < 1:
        quantity = 1

    cart = request.session.get('cart', {})
    current = cart.get(str(product_id), 0)
    requested = current + quantity

    # Cap the total quantity at what's actually in stock.
    if requested > product.stock:
        cart[str(product_id)] = product.stock
        if product.stock == 0:
            cart.pop(str(product_id), None)
            messages.warning(request, f'Sorry, {product.name} is out of stock.')
        else:
            messages.warning(
                request,
                f'Only {product.stock} of {product.name} in stock — '
                f'quantity set to {product.stock}.'
            )
    else:
        cart[str(product_id)] = requested
        basket_url = reverse('view_cart')
        messages.success(request, mark_safe(
            f'Added {product.name} to your basket. '
            f'<a href="{basket_url}" class="alert-link">View basket</a>'
        ))

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """Set the quantity of a product in the cart, capped at available stock."""
    product = get_object_or_404(Product, pk=product_id)

    try:
        quantity = int(request.POST.get('quantity', 0))
    except (TypeError, ValueError):
        quantity = 0

    cart = request.session.get('cart', {})

    if quantity <= 0:
        cart.pop(str(product_id), None)
        messages.success(request, f'Removed {product.name} from your cart.')
    elif quantity > product.stock:
        # Requested more than available: cap at stock.
        cart[str(product_id)] = product.stock
        messages.warning(
            request,
            f'Only {product.stock} of {product.name} in stock — '
            f'quantity set to {product.stock}.'
        )
    else:
        cart[str(product_id)] = quantity
        messages.success(request, f'Updated {product.name} quantity to {quantity}.')

    request.session['cart'] = cart
    return redirect('view_cart')


def remove_from_cart(request, product_id):
    """Remove a product from the cart entirely."""
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    messages.success(request, f'Removed {product.name} from your cart.')
    return redirect('view_cart')