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
    'creatine-monohydrate-500g': 'creatine-monohydrate.webp',
    'electrolyte-hydration-tablets': 'electrolyte-hydration.webp',
    'performance-training-t-shirt-fithub': 'performance-shirt.webp',
    'gym-towel-bottle-set': 'towel-bottle.webp',
    'stainless-steel-water-bottle-750ml': 'water-bottle.webp',
    'compression-leggings': 'compression-leggings.webp',
    'yoga-mat': 'yoga-mat.webp',
    'skipping-rope': 'skipping-rope.webp',
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