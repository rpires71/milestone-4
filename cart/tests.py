"""Tests for the cart app: basket operations and stock limits."""

from django.test import TestCase
# reverse() builds a URL from its name â€” so tests don't hardcode paths.
from django.urls import reverse

from cart.contexts import cart_contents
from shop.models import Product


class CartViewTest(TestCase):
    """Tests for the cart add/adjust/remove views (session-based)."""

    def setUp(self):
        # One test product, rebuilt fresh before every test (DB resets between tests).
        # stock=50 gives headroom so most tests aren't accidentally hitting the cap.
        self.product = Product.objects.create(
            name='Test Kettlebell',
            slug='test-kettlebell',
            description='A test product.',
            price=29.99,
            stock=50,
        )

    def test_add_to_cart(self):
        """Posting a product adds it to the session cart with the quantity."""
        # self.client is Django's TEST CLIENT â€” it simulates a browser making
        # HTTP requests, WITHOUT a real server. .post() sends a POST request.
        response = self.client.post(
            # reverse('add_to_cart', args=[id]) builds the URL, injecting the
            # product id as the URL argument.
            reverse('add_to_cart', args=[self.product.id]),
            {'quantity': 2, 'redirect_url': '/'},   # the POST body (form data)
        )
        # 302 = redirect. Adding to cart redirects back (PRG pattern), so we
        # expect 302, not 200.
        self.assertEqual(response.status_code, 302)
        # self.client.session lets the test inspect the session the view wrote to.
        # Note the KEY IS A STRING (str(id)) â€” session dict keys are always strings.
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 2)

    def test_add_existing_product_increments_quantity(self):
        """Adding a product already in the cart increases its quantity."""
        # Add 1, then add 3 more â€” the view should ACCUMULATE to 4, not overwrite to 3.
        # This tests behaviour that a single add couldn't reveal.
        self.client.post(reverse('add_to_cart', args=[self.product.id]),
                         {'quantity': 1, 'redirect_url': '/'})
        self.client.post(reverse('add_to_cart', args=[self.product.id]),
                         {'quantity': 3, 'redirect_url': '/'})
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 4)   # 1 + 3

    def test_adjust_cart_updates_quantity(self):
        """Adjusting to a positive quantity updates the session cart."""
        # ARRANGE the session directly: instead of adding via the view, we set
        # the cart state manually. This isolates the ADJUST behaviour from ADD.
        # session.save() is REQUIRED â€” without it, the change isn't persisted.
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(reverse('adjust_cart', args=[self.product.id]),
                                    {'quantity': 5})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 5)

    def test_adjust_cart_to_zero_removes_item(self):
        """Adjusting the quantity to zero removes the item from the cart."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()
        self.client.post(reverse('adjust_cart', args=[self.product.id]),
                         {'quantity': 0})
        # assertNotIn checks the key is GONE â€” setting quantity to 0 should
        # remove the item entirely, not leave it at 0.
        self.assertNotIn(str(self.product.id), self.client.session['cart'])

    def test_remove_from_cart(self):
        """Removing a product clears it from the session cart."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()
        response = self.client.post(reverse('remove_from_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(str(self.product.id), self.client.session['cart'])

    def test_view_cart_page_loads(self):
        """The cart page returns a 200 response."""
        # A GET (not POST) â€” just checking the page renders. A "smoke test":
        # confirms the view doesn't crash and returns 200.
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)

    # ---- STOCK CAPPING TESTS (these prove defect D5's fix) ----

    def test_add_caps_at_available_stock(self):
        """Adding more than the available stock caps the quantity at stock."""
        self.product.stock = 5
        self.product.save()
        # Try to add 20 when only 5 exist...
        self.client.post(reverse('add_to_cart', args=[self.product.id]),
                         {'quantity': 20, 'redirect_url': '/'})
        # ...the cart should hold 5, not 20. This is the stock cap working.
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 5)

    def test_adjust_caps_at_available_stock(self):
        """Adjusting above available stock caps the quantity at stock."""
        self.product.stock = 5
        self.product.save()
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()
        self.client.post(reverse('adjust_cart', args=[self.product.id]),
                         {'quantity': 99})
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 5)

    def test_add_out_of_stock_product_not_added(self):
        """A product with zero stock is not added to the cart."""
        self.product.stock = 0
        self.product.save()
        self.client.post(reverse('add_to_cart', args=[self.product.id]),
                         {'quantity': 1, 'redirect_url': '/'})
        # .get('cart', {}) because the cart might not exist at all if nothing
        # was ever added â€” avoids a KeyError.
        cart = self.client.session.get('cart', {})
        self.assertNotIn(str(self.product.id), cart)

    # ---- MALICIOUS / BAD INPUT TESTS (robustness â€” this is distinction-flavoured) ----

    def test_add_with_non_numeric_quantity_defaults_to_one(self):
        """A non-numeric quantity does not crash; the default of 1 is applied."""
        # Someone sends quantity='abc' (e.g. tampering with the form). The view
        # must NOT crash â€” it should fall back to 1. This tests defensive coding.
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]),
                                    {'quantity': 'abc', 'redirect_url': '/'})
        self.assertEqual(response.status_code, 302)   # didn't 500-crash
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 1)

    def test_add_with_negative_quantity_defaults_to_one(self):
        """A negative quantity is clamped to the default of 1."""
        self.client.post(reverse('add_to_cart', args=[self.product.id]),
                         {'quantity': -5, 'redirect_url': '/'})
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 1)

    def test_adjust_with_non_numeric_quantity_removes_item(self):
        """A non-numeric adjustment does not crash; it falls back to 0 (removal)."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]),
                                    {'quantity': 'abc'})
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(str(self.product.id), self.client.session['cart'])

    def test_adjust_with_negative_quantity_removes_item(self):
        """A negative adjustment is treated as zero and removes the item."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()
        self.client.post(reverse('adjust_cart', args=[self.product.id]),
                         {'quantity': -3})
        self.assertNotIn(str(self.product.id), self.client.session['cart'])

    def test_get_request_rejected_on_add(self):
        """State-changing cart actions reject GET requests (require POST)."""
        response = self.client.get(
            reverse('add_to_cart', args=[self.product.id])
        )
        self.assertEqual(response.status_code, 405)  # 405 Method Not Allowed


class CartContextProcessorTest(TestCase):
    """Tests for the cart_contents context processor."""

    def setUp(self):
        # A Â£10 product with default stock â€” used to check total arithmetic.
        self.product = Product.objects.create(
            name='Test Mat', slug='test-mat',
            description='A test product.', price=10.00,
        )

    def test_empty_cart_totals(self):
        """An empty cart returns zero total and zero product count."""
        # Here we test the context processor DIRECTLY as a function, not through
        # a view. We need a request object, so we grab one from the test client
        # (.wsgi_request), set an empty cart, and call cart_contents(request).
        request = self.client.get('/').wsgi_request
        request.session['cart'] = {}
        context = cart_contents(request)
        # Verify all three returned values are the empty-state defaults.
        self.assertEqual(context['product_count'], 0)
        self.assertEqual(context['total'], 0)
        self.assertEqual(context['cart_items'], [])

    def test_populated_cart_totals(self):
        """A populated cart computes the correct total and product count."""
        request = self.client.get('/').wsgi_request
        request.session['cart'] = {str(self.product.id): 3}
        context = cart_contents(request)
        # 3 items, Â£10 each -> total 30, count 3, one line with subtotal 30.
        # This proves the arithmetic in contexts.py is correct.
        self.assertEqual(context['product_count'], 3)
        self.assertEqual(context['total'], 30.00)
        self.assertEqual(len(context['cart_items']), 1)
        self.assertEqual(context['cart_items'][0]['subtotal'], 30.00)
