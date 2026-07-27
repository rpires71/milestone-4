# The views.py file contains the view functions for the Home application.
# Each view receives an HTTP request, processes any required application
# logic, retrieves data where necessary and returns an HTTP response. In
# this application, the views are responsible for rendering the homepage
# together with static informational pages such as the Terms and
# Conditions and Privacy Policy.

from django.shortcuts import render

# Import the Plan model so that published subscription plans can be
# retrieved and displayed on the homepage.
from plans.models import Plan

# Import the Product model so that available products can be displayed
# on the homepage.
from shop.models import Product


def index(request):
    """
    Render the FitHub homepage with featured subscription plans and
    featured products.
    """

    # Retrieve the first three published subscription plans to feature
    # on the homepage.
    featured_plans = Plan.objects.filter(status='published')[:3]

    # Retrieve the first four products that are currently available for
    # purchase.
    featured_products = Product.objects.filter(is_available=True)[:4]

    # Store the retrieved data in a context dictionary so that it can be
    # accessed by the homepage template during rendering.
    context = {
        'featured_plans': featured_plans,
        'featured_products': featured_products,
    }

    # Render the homepage template and pass the context data to the
    # template engine.
    return render(request, 'home/index.html', context)


def terms(request):
    """
    Render the application's static Terms and Conditions page.
    """

    # Return the Terms and Conditions template.
    return render(request, 'home/terms.html')


def privacy(request):
    """
    Render the application's static Privacy Policy page.
    """

    # Return the Privacy Policy template.
    return render(request, 'home/privacy.html')
