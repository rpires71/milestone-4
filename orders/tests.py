from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from shop.models import Product
from orders.models import Order, OrderLineItem


class OrderModelTest(TestCase):
    """Tests for the Order and OrderLineItem models."""

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Weight',
            slug='test-weight',
            description='A test product.',
            price=25.00,
        )
        self.order = Order.objects.create(
            order_number='ABC123',
            full_name='Jane Doe',
            email='jane@example.com',
            address_line1='1 Test Street',
            town_city='Testville',
            postcode='TE5 7ST',
            country='UK',
            subtotal=25.00,
            total=25.00,
        )

    def test_order_str(self):
        """The order __str__ returns its order number."""
        self.assertEqual(str(self.order), 'ABC123')

    def test_order_defaults(self):
        """A new order defaults to 'processing' status."""
        self.assertEqual(self.order.status, 'processing')

    def test_line_item_relationship(self):
        """Line items are accessible via the order's related name."""
        item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price=25.00,
        )
        self.assertIn(item, self.order.line_items.all())
        self.assertEqual(self.order.line_items.count(), 1)


class CheckoutViewTest(TestCase):
    """Tests for the checkout and checkout_success views."""

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Rope',
            slug='test-rope',
            description='A test product.',
            price=12.00,
        )

    def test_empty_cart_redirects(self):
        """Checkout with an empty cart redirects away (to products)."""
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    @patch('orders.views.stripe.PaymentIntent.create')
    def test_checkout_page_loads_with_items(self, mock_intent):
        """With items in the cart, the checkout page loads (Stripe mocked)."""
        # Fake the Stripe PaymentIntent so no real API call is made.
        mock_intent.return_value = type(
            'FakeIntent', (), {'client_secret': 'test_secret_123'}
        )()

        session = self.client.session
        session['cart'] = {str(self.product.id): 1}
        session.save()

        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        mock_intent.assert_called_once()

    def test_checkout_post_creates_order(self):
        """A valid POST creates an order and line items, and clears the cart."""
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()

        form_data = {
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'phone': '01234567890',
            'address_line1': '5 Example Road',
            'address_line2': '',
            'town_city': 'Sampleton',
            'postcode': 'SA1 2PL',
            'country': 'UK',
        }
        response = self.client.post(reverse('checkout'), form_data)

        # An order was created with one line item for the cart product.
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.line_items.count(), 1)
        self.assertEqual(order.line_items.first().quantity, 2)
        self.assertEqual(order.total, 24.00)

        # The cart is cleared and the user is redirected to success.
        self.assertEqual(self.client.session['cart'], {})
        self.assertEqual(response.status_code, 302)

    def test_checkout_deducts_stock(self):
        """Completing checkout reduces each product's stock by the quantity sold."""
        self.product.stock = 10
        self.product.save()

        session = self.client.session
        session['cart'] = {str(self.product.id): 3}
        session.save()

        form_data = {
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'phone': '01234567890',
            'address_line1': '5 Example Road',
            'address_line2': '',
            'town_city': 'Sampleton',
            'postcode': 'SA1 2PL',
            'country': 'UK',
        }
        self.client.post(reverse('checkout'), form_data)

        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 7)

    def test_checkout_stock_never_negative(self):
        """Stock is clamped at zero and never goes negative on oversell."""
        self.product.stock = 2
        self.product.save()

        session = self.client.session
        session['cart'] = {str(self.product.id): 5}
        session.save()

        form_data = {
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'phone': '01234567890',
            'address_line1': '5 Example Road',
            'address_line2': '',
            'town_city': 'Sampleton',
            'postcode': 'SA1 2PL',
            'country': 'UK',
        }
        self.client.post(reverse('checkout'), form_data)

        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 0)

    def test_checkout_success_page(self):
        """The success page displays the order number."""
        order = Order.objects.create(
            order_number='SUCCESS123',
            full_name='Jane Doe',
            email='jane@example.com',
            address_line1='1 Test Street',
            town_city='Testville',
            postcode='TE5 7ST',
            country='UK',
            subtotal=12.00,
            total=12.00,
        )
        response = self.client.get(
            reverse('checkout_success', args=[order.order_number])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'SUCCESS123')