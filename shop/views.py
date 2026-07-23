from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, render

from .models import Product


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
    """Display an individual product with a few related products."""
    product = get_object_or_404(Product, slug=slug, is_available=True)
    # "Customers also viewed" - other available products, same category first
    related = Product.objects.filter(
        is_available=True
    ).exclude(pk=product.pk)
    if product.category_id:
        same_cat = list(related.filter(category_id=product.category_id)[:4])
    else:
        same_cat = []
    if len(same_cat) < 4:
        extra = related.exclude(pk__in=[p.pk for p in same_cat])[:4 - len(same_cat)]
        same_cat = same_cat + list(extra)
    context = {'product': product, 'related_products': same_cat}
    return render(request, 'shop/product_detail.html', context)
