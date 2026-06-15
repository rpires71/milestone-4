from django.shortcuts import render
from .models import Product


def all_products(request):
    """Display all available products."""
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'shop/products.html', context)