from .models import Product
from django.shortcuts import render, get_object_or_404


def all_products(request):
    """Display all available products."""
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'shop/products.html', context)


def product_detail(request, slug):
    """Display an individual product."""
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'shop/product_detail.html', {'product': product})