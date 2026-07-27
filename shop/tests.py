# The tests.py file verifies the behaviour of the Shop application at
# both model and view levels. These tests confirm that products and
# categories are stored correctly, relationships are maintained and the
# shop pages display only products that are available for purchase.

from django.test import TestCase
from django.urls import reverse

# Import the models being tested.
from shop.models import Product, ProductCategory


class ShopModelTest(TestCase):
    """
    Test the ProductCategory and Product models.

    Model tests verify that default values, relationships and string
    representations behave as expected before the models are used by
    views, templates and the checkout process.
    """

    def setUp(self):
        """
        Create reusable category and product objects before each test.

        Using setUp() reduces duplicated code and ensures that every test
        begins with a predictable dataset.
        """
        self.category, _ = ProductCategory.objects.get_or_create(
            slug='equipment',
            defaults={
                'name': 'Equipment',
            },
        )

        self.product = Product.objects.create(
            category=self.category,
            name='Test Barbell',
            slug='test-barbell',
            description='A test product.',
            price=99.99,
        )

    def test_category_str(self):
        """
        Confirm that the ProductCategory string representation returns the
        category name.
        """
        self.assertEqual(
            str(self.category),
            'Equipment',
        )

    def test_product_str(self):
        """
        Confirm that the Product string representation returns the product
        name.
        """
        self.assertEqual(
            str(self.product),
            'Test Barbell',
        )

    def test_product_defaults(self):
        """
        Confirm that newly created products are available by default and
        begin with zero stock unless specified otherwise.
        """
        self.assertTrue(self.product.is_available)
        self.assertEqual(self.product.stock, 0)

    def test_category_product_relationship(self):
        """
        Confirm that a product can be accessed through its category using
        the configured related name.

        This verifies that the foreign key relationship has been created
        correctly.
        """
        self.assertIn(
            self.product,
            self.category.products.all(),
        )


class ShopViewTest(TestCase):
    """
    Test the shop catalogue and product detail views.

    These tests verify that customers can browse available products while
    preventing unavailable or non-existent products from being displayed.
    """

    def setUp(self):
        """
        Create one available and one unavailable product for use across
        the view tests.
        """
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
        """
        Confirm that the product catalogue page loads successfully.
        """
        response = self.client.get(
            reverse('products')
        )

        self.assertEqual(response.status_code, 200)

    def test_products_page_shows_available_only(self):
        """
        Confirm that only products marked as available are displayed in
        the shop catalogue.

        Products that have been hidden from sale should not appear in the
        public product listing.
        """
        response = self.client.get(
            reverse('products')
        )

        self.assertContains(
            response,
            'Available Product',
        )

        self.assertNotContains(
            response,
            'Hidden Product',
        )

    def test_product_detail_loads(self):
        """
        Confirm that the detail page for an available product loads
        successfully.
        """
        response = self.client.get(
            reverse(
                'product_detail',
                args=[self.available.slug],
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Available Product',
        )

    def test_unavailable_product_detail_returns_404(self):
        """
        Confirm that products marked as unavailable cannot be viewed
        directly and return a 404 response instead.
        """
        response = self.client.get(
            reverse(
                'product_detail',
                args=[self.unavailable.slug],
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_invalid_slug_returns_404(self):
        """
        Confirm that requesting a non-existent product slug returns a
        404 response.

        This prevents invalid URLs from exposing unintended information
        and demonstrates appropriate error handling.
        """
        response = self.client.get(
            reverse(
                'product_detail',
                args=['does-not-exist'],
            )
        )

        self.assertEqual(response.status_code, 404)
