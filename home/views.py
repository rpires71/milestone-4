from django.shortcuts import render
from plans.models import Plan
from shop.models import Product


def index(request):
    """Render the FitHub homepage with featured plans and products."""
    featured_plans = Plan.objects.filter(status='published')[:3]
    featured_products = Product.objects.filter(is_available=True)[:4]
    context = {
        'featured_plans': featured_plans,
        'featured_products': featured_products,
    }
    return render(request, 'home/index.html', context)


def terms(request):
    """Static Terms & Conditions page."""
    return render(request, 'home/terms.html')


def privacy(request):
    """Static Privacy Policy page."""
    return render(request, 'home/privacy.html')