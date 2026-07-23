"""Custom template tags/filters for the plans app."""
from django import template
from django.templatetags.static import static
from django.contrib.staticfiles import finders

register = template.Library()

# Maps a plan slug to its static image filename in static/images/plans/
PLAN_IMAGE_MAP = {
    'starter': 'starter.webp',
    'premium': 'premium.webp',
    'elite': 'elite.webp',
    'annual-pro': 'annual-pro.webp',
}


@register.filter
def plan_image(slug):
    """Return the static URL for a plan's image, or '' if none mapped/found."""
    filename = PLAN_IMAGE_MAP.get(slug)
    if not filename:
        return ''
    path = f'images/plans/{filename}'
    if finders.find(path):
        return static(path)
    return ''
