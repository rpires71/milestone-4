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