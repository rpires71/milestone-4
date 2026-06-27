"""Custom template tags/filters for the shop app."""
from django import template
from django.templatetags.static import static
from django.contrib.staticfiles import finders

register = template.Library()

# Maps a product slug to its static image filename in static/images/products/
PRODUCT_IMAGE_MAP = {
    'adjustable-dumbbell-set-24kg': 'dumbbell.webp',
    'kettlebell-16kg': 'kettlebell-16kg.webp',
    'resistance-bands-set': 'resistance-band.webp',
    'whey-protein-powder-1kg-chocolate': 'protein-shaker.webp',
    # Add more slug -> filename pairs here as you add product images.
}


@register.filter
def product_image(slug):
    """Return the static URL for a product's image, or '' if none mapped/found."""
    filename = PRODUCT_IMAGE_MAP.get(slug)
    if not filename:
        return ''
    path = f'images/products/{filename}'
    # Only return a URL if the file actually exists in static files
    if finders.find(path):
        return static(path)
    return ''