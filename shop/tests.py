from django.test import TestCase
from django.urls import reverse

from shop.models import Product, ProductCategory


class ShopModelTest(TestCase):
    """Tests for the ProductCategory and Product models."""

    def setUp(self):
        self.category, _ = ProductCategory.objects.get_or_create(
            slug='equipment', defaults={'name': 'Equipment'}
        )
        self.product = Product.objects.create(
            category=self.category,
            name='Test Barbell',
            slug='test-barbell',
            description='A test product.',
            price=99.99,
        )

    def test_category_str(self):
        """The category __str__ returns its name."""
        self.assertEqual(str(self.category), 'Equipment')

    def test_product_str(self):
        """The product __str__ returns its name."""
        self.assertEqual(str(self.product), 'Test Barbell')

    def test_product_defaults(self):
        """A product defaults to available with zero stock."""
        self.assertTrue(self.product.is_available)
        self.assertEqual(self.product.stock, 0)

    def test_category_product_relationship(self):
        """A product is accessible via the category's related name."""
        self.assertIn(self.product, self.category.products.all())


class ShopViewTest(TestCase):
    """Tests for the all_products and product_detail views."""

    def setUp(self):
        self.available = Product.objects.create(
            name='Available Product',
            slug='available-product',
            description='In stock.',
            price=20.00,
            is_available=True,
        )
        self.unavailable = Product.objects.create(
            name='Hidden Product',
            slug='hidden-product',
            description='Not for sale.',
            price=20.00,
            is_available=False,
        )

    def test_products_page_loads(self):
        """The products list page returns a 200 response."""
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_products_page_shows_available_only(self):
        """The products list includes available products and excludes hidden ones."""
        response = self.client.get(reverse('products'))
        self.assertContains(response, 'Available Product')
        self.assertNotContains(response, 'Hidden Product')

    def test_product_detail_loads(self):
        """An available product's detail page returns a 200 response."""
        response = self.client.get(
            reverse('product_detail', args=[self.available.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Available Product')

    def test_unavailable_product_detail_returns_404(self):
        """An unavailable product's detail page returns a 404."""
        response = self.client.get(
            reverse('product_detail', args=[self.unavailable.slug])
        )
        self.assertEqual(response.status_code, 404)

    def test_invalid_slug_returns_404(self):
        """A non-existent slug returns a 404."""
        response = self.client.get(
            reverse('product_detail', args=['does-not-exist'])
        )
        self.assertEqual(response.status_code, 404)
