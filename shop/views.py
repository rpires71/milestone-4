from .models import Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count


def all_products(request):
    """Display all available products with average rating annotation."""
    products = Product.objects.filter(is_available=True).annotate(
        avg_rating=Avg('reviews__rating'),
        review_count=Count('reviews'),
    )
    context = {
        'products': products,
    }
    return render(request, 'shop/products.html', context)


def product_detail(request, slug):
    """Display an individual product."""
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'shop/product_detail.html', {'product': product})
