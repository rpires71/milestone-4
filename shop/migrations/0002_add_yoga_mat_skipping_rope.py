from django.db import migrations
from django.utils.text import slugify


def add_products(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    ProductCategory = apps.get_model('shop', 'ProductCategory')

    def get_category(name):
        # Match existing category by name (works across SQLite and Postgres).
        # If it doesn't exist (e.g. a fresh database), create it with a slug,
        # since ProductCategory.slug is unique and required.
        cat = ProductCategory.objects.filter(name=name).first()
        if cat is None:
            cat = ProductCategory.objects.create(name=name, slug=slugify(name))
        return cat

    products = [
        {
            'slug': 'yoga-mat',
            'name': 'Yoga Mat',
            'category': get_category('Accessories'),
            'brand': 'FitHub',
            'price': '24.99',
            'stock': 25,
            'description': ('A non-slip, cushioned yoga mat for floor work, '
                            'stretching and recovery sessions at home or in the gym.'),
            'is_available': True,
        },
        {
            'slug': 'skipping-rope',
            'name': 'Skipping Rope',
            'category': get_category('Equipment'),
            'brand': 'FitHub',
            'price': '12.99',
            'stock': 25,
            'description': ('An adjustable-length speed skipping rope for cardio, '
                            'conditioning and warm-ups.'),
            'is_available': True,
        },
    ]

    for data in products:
        # keyed on slug -> safe to run repeatedly, never duplicates
        Product.objects.get_or_create(slug=data['slug'], defaults=data)


def remove_products(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    Product.objects.filter(slug__in=['yoga-mat', 'skipping-rope']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_products, remove_products),
    ]
