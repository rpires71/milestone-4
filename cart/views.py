from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from shop.models import Product


def view_cart(request):
    """Display the current shopping cart."""
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """Add a quantity of a product to the cart."""
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[str(product_id)]}')
    else:
        cart[str(product_id)] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """Adjust the quantity of a product in the cart."""
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 0))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[str(product_id)] = quantity
        messages.success(request, f'Updated {product.name} quantity to {quantity}')
    else:
        cart.pop(str(product_id), None)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect('view_cart')


def remove_from_cart(request, product_id):
    """Remove a product from the cart entirely."""
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    messages.success(request, f'Removed {product.name} from your cart')
    return redirect('view_cart')