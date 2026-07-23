"""Tests for the cart app: basket operations and stock limits."""

from django.test import TestCase
from django.urls import reverse

from cart.contexts import cart_contents
from shop.models import Product


class CartViewTest(TestCase):
    """Tests for the cart add/adjust/remove views (session-based)."""

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Kettlebell',
            slug='test-kettlebell',
            description='A test product.',
            price=29.99,
            stock=50,
        )

    def test_add_to_cart(self):
        """Posting a product adds it to the session cart with the quantity."""
        response = self.client.post(
            reverse('add_to_cart', args=[self.product.id]),
            {'quantity': 2, 'redirect_url': '/'},
        )
        self.assertEqual(response.status_code, 302)
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 2)

    def test_add_existing_product_increments_quantity(self):
        """Adding a product already in the cart increases its quantity."""
        self.client.post(
            reverse('add_to_cart', args=[self.product.id]),
            {'quantity': 1, 'redirect_url': '/'},
        )
        self.client.post(
            reverse('add_to_cart', args=[self.product.id]),
            {'quantity': 3, 'redirect_url': '/'},
        )
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 4)

    def test_adjust_cart_updates_quantity(self):
        """Adjusting to a positive quantity updates the session cart."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(
            reverse('adjust_cart', args=[self.product.id]),
            {'quantity': 5},
        )
        self.assertEqual(response.status_code, 302)
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 5)

    def test_adjust_cart_to_zero_removes_item(self):
        """Adjusting the quantity to zero removes the item from the cart."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()

        self.client.post(
            reverse('adjust_cart', args=[self.product.id]),
            {'quantity': 0},
        )
        cart = self.client.session['cart']
        self.assertNotIn(str(self.product.id), cart)

    def test_remove_from_cart(self):
        """Removing a product clears it from the session cart."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(
            reverse('remove_from_cart', args=[self.product.id])
        )
        self.assertEqual(response.status_code, 302)
        cart = self.client.session['cart']
        self.assertNotIn(str(self.product.id), cart)

    def test_view_cart_page_loads(self):
        """The cart page returns a 200 response."""
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)

    def test_add_caps_at_available_stock(self):
        """Adding more than the available stock caps the quantity at stock."""
        self.product.stock = 5
        self.product.save()
        self.client.post(
            reverse('add_to_cart', args=[self.product.id]),
            {'quantity': 20, 'redirect_url': '/'},
        )
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 5)

    def test_adjust_caps_at_available_stock(self):
        """Adjusting above available stock caps the quantity at stock."""
        self.product.stock = 5
        self.product.save()
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()
        self.client.post(
            reverse('adjust_cart', args=[self.product.id]),
            {'quantity': 99},
        )
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 5)

    def test_add_out_of_stock_product_not_added(self):
        """A product with zero stock is not added to the cart."""
        self.product.stock = 0
        self.product.save()
        self.client.post(
            reverse('add_to_cart', args=[self.product.id]),
            {'quantity': 1, 'redirect_url': '/'},
        )
        cart = self.client.session.get('cart', {})
        self.assertNotIn(str(self.product.id), cart)

    def test_add_with_non_numeric_quantity_defaults_to_one(self):
        """A non-numeric quantity does not crash; the default of 1 is applied."""
        response = self.client.post(
            reverse('add_to_cart', args=[self.product.id]),
            {'quantity': 'abc', 'redirect_url': '/'},
        )
        self.assertEqual(response.status_code, 302)
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 1)

    def test_add_with_negative_quantity_defaults_to_one(self):
        """A negative quantity is clamped to the default of 1."""
        response = self.client.post(
            reverse('add_to_cart', args=[self.product.id]),
            {'quantity': -5, 'redirect_url': '/'},
        )
        self.assertEqual(response.status_code, 302)
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 1)

    def test_adjust_with_non_numeric_quantity_removes_item(self):
        """A non-numeric adjustment does not crash; it falls back to 0 (removal)."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(
            reverse('adjust_cart', args=[self.product.id]),
            {'quantity': 'abc'},
        )
        self.assertEqual(response.status_code, 302)
        cart = self.client.session['cart']
        self.assertNotIn(str(self.product.id), cart)

    def test_adjust_with_negative_quantity_removes_item(self):
        """A negative adjustment is treated as zero and removes the item."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()

        self.client.post(
            reverse('adjust_cart', args=[self.product.id]),
            {'quantity': -3},
        )
        cart = self.client.session['cart']
        self.assertNotIn(str(self.product.id), cart)


class CartContextProcessorTest(TestCase):
    """Tests for the cart_contents context processor."""

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Mat',
            slug='test-mat',
            description='A test product.',
            price=10.00,
        )

    def test_empty_cart_totals(self):
        """An empty cart returns zero total and zero product count."""
        request = self.client.get('/').wsgi_request
        request.session['cart'] = {}
        context = cart_contents(request)
        self.assertEqual(context['product_count'], 0)
        self.assertEqual(context['total'], 0)
        self.assertEqual(context['cart_items'], [])

    def test_populated_cart_totals(self):
        """A populated cart computes the correct total and product count."""
        request = self.client.get('/').wsgi_request
        request.session['cart'] = {str(self.product.id): 3}
        context = cart_contents(request)
        self.assertEqual(context['product_count'], 3)
        self.assertEqual(context['total'], 30.00)
        self.assertEqual(len(context['cart_items']), 1)
        self.assertEqual(context['cart_items'][0]['subtotal'], 30.00)
