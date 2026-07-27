# The views.py file contains the request-handling logic for the Shop
# application. It retrieves product information from the database and
# prepares it for presentation within the product catalogue and product
# detail pages. Additional query annotations and related-product logic
# enhance the shopping experience by providing customer review summaries
# and product recommendations.

from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, render

# Import the Product model used to retrieve shop items from the database.
from .models import Product


def all_products(request):
    """
    Display all products that are currently available for purchase.

    The product queryset is annotated with the average customer rating
    and total number of reviews, allowing this information to be
    displayed efficiently without requiring additional database queries
    within the template.
    """

    # Retrieve only products that are available for sale and calculate
    # summary review statistics for each product.
    products = Product.objects.filter(
        is_available=True
    ).annotate(
        avg_rating=Avg('reviews__rating'),
        review_count=Count('reviews'),
    )

    # Package the queryset into a context dictionary for the template.
    context = {
        'products': products,
    }

    return render(
        request,
        'shop/products.html',
        context,
    )


def product_detail(request, slug):
    """
    Display the detail page for a single available product.

    In addition to the selected product, a small collection of related
    products is generated to encourage customers to continue browsing the
    shop.
    """

    # Retrieve the requested product using its unique slug. Products that
    # are unavailable cannot be accessed through the public catalogue.
    product = get_object_or_404(
        Product,
        slug=slug,
        is_available=True,
    )

    # Begin building a list of related products by selecting all other
    # available products while excluding the current product.
    related = Product.objects.filter(
        is_available=True,
    ).exclude(
        pk=product.pk,
    )

    # Give priority to products that belong to the same category, as they
    # are more likely to be relevant to the customer's interests.
    if product.category_id:
        same_cat = list(
            related.filter(
                category_id=product.category_id,
            )[:4]
        )
    else:
        same_cat = []

    # If fewer than four products exist within the same category,
    # supplement the list with other available products so that the
    # recommendation section remains populated.
    if len(same_cat) < 4:
        extra = related.exclude(
            pk__in=[p.pk for p in same_cat]
        )[:4 - len(same_cat)]

        same_cat = same_cat + list(extra)

    # Prepare the selected product and recommended products for
    # presentation within the template.
    context = {
        'product': product,
        'related_products': same_cat,
    }

    return render(
        request,
        'shop/product_detail.html',
        context,
    )
