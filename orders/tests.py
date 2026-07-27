# The tests.py file contains automated tests for the Orders application.
# These tests verify the behaviour of the order models, checkout workflow,
# stock management, success page and authenticated order history views.
#
# Automated testing is important because the checkout process changes several
# related parts of the application, including database records, session data,
# stock values and redirects. Testing these behaviours helps prevent
# regressions when the application is modified or deployed.

"""Tests for the orders app: checkout, stock handling and order history."""

# Import patch so external Stripe calls can be replaced with controlled
# test objects. This prevents automated tests from contacting the real
# Stripe API.
from unittest.mock import patch

# Import Django's TestCase, which provides an isolated test database and
# a test client for simulating browser requests.
from django.test import TestCase

# Import reverse so URLs are resolved by their route names rather than
# being hard-coded into the tests.
from django.urls import reverse

# Import the order models used to create and inspect test records.
from orders.models import Order, OrderLineItem

# Import Product so checkout tests can create catalogue items and verify
# stock changes.
from shop.models import Product


class OrderModelTest(TestCase):
    """
    Test the behaviour and relationships of the Order and OrderLineItem
    models independently of the checkout views.
    """

    def setUp(self):
        """
        Create reusable product and order records before each model test.

        Django resets the test database between tests, ensuring that each
        test runs independently with predictable data.
        """

        # Create a product that can be associated with an order line item.
        self.product = Product.objects.create(
            name='Test Weight',
            slug='test-weight',
            description='A test product.',
            price=25.00,
        )

        # Create a completed order with known values so model behaviour can
        # be tested consistently.
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
        """
        Confirm that the Order model's string representation returns its
        unique order number.
        """

        # A readable string representation improves how orders are displayed
        # in Django administration and debugging output.
        self.assertEqual(str(self.order), 'ABC123')

    def test_order_defaults(self):
        """
        Confirm that a newly created order uses the expected default status.
        """

        # New orders should begin in the processing stage until an
        # administrator updates their fulfilment status.
        self.assertEqual(self.order.status, 'processing')

    def test_line_item_relationship(self):
        """
        Confirm that order line items can be accessed through the Order
        model's related_name.
        """

        # Arrange: create one line item linked to the existing order.
        item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price=25.00,
        )

        # Assert that the related_name provides access to the created item.
        self.assertIn(item, self.order.line_items.all())

        # Confirm that exactly one line item is associated with the order.
        self.assertEqual(self.order.line_items.count(), 1)


class CheckoutViewTest(TestCase):
    """
    Test the checkout and checkout-success views, including cart handling,
    form validation, order creation and stock updates.
    """

    def setUp(self):
        """
        Create a reusable product before each checkout test.
        """

        # The product provides a predictable price for calculating order
        # totals and testing stock deductions.
        self.product = Product.objects.create(
            name='Test Rope',
            slug='test-rope',
            description='A test product.',
            price=12.00,
        )

    def test_empty_cart_redirects(self):
        """
        Confirm that users cannot access checkout when their cart is empty.
        """

        # Act: request the checkout page without adding products to the
        # session cart.
        response = self.client.get(reverse('checkout'))

        # Assert: the view should redirect rather than display an empty
        # checkout form.
        self.assertEqual(response.status_code, 302)

    @patch('orders.views.stripe.PaymentIntent.create')
    def test_checkout_page_loads_with_items(self, mock_intent):
        """
        Confirm that checkout loads when the cart contains products and that
        a Stripe Payment Intent is created.
        """

        # Replace Stripe's real PaymentIntent response with a simple test
        # object containing the client secret expected by the view.
        mock_intent.return_value = type(
            'FakeIntent',
            (),
            {'client_secret': 'test_secret_123'}
        )()

        # Arrange: store one product in the test client's session cart.
        session = self.client.session
        session['cart'] = {str(self.product.id): 1}
        session.save()

        # Act: request the checkout page.
        response = self.client.get(reverse('checkout'))

        # Assert: the checkout page should render successfully.
        self.assertEqual(response.status_code, 200)

        # Confirm that the view attempted to create exactly one Stripe
        # Payment Intent.
        mock_intent.assert_called_once()

    def test_checkout_post_creates_order(self):
        """
        Confirm that valid checkout details create an order and line item,
        calculate the total, clear the cart and redirect the user.
        """

        # Arrange: place two units of the product in the session cart.
        session = self.client.session
        session['cart'] = {str(self.product.id): 2}
        session.save()

        # Provide valid customer and delivery details.
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

        # Act: submit the checkout form.
        response = self.client.post(
            reverse('checkout'),
            form_data
        )

        # Assert that one Order record was created.
        self.assertEqual(Order.objects.count(), 1)

        # Retrieve the created order for detailed checks.
        order = Order.objects.first()

        # Confirm that the order contains one line item representing the
        # selected product.
        self.assertEqual(order.line_items.count(), 1)

        # Confirm that the selected quantity was stored correctly.
        self.assertEqual(order.line_items.first().quantity, 2)

        # Confirm that the order total equals two products at £12 each.
        self.assertEqual(order.total, 24.00)

        # Confirm that the session cart was cleared after successful checkout.
        self.assertEqual(self.client.session['cart'], {})

        # Confirm that the user was redirected to the success page.
        self.assertEqual(response.status_code, 302)

    def test_checkout_deducts_stock(self):
        """
        Confirm that successful checkout reduces product stock by the
        quantity purchased.
        """

        # Arrange: begin with a known stock quantity.
        self.product.stock = 10
        self.product.save()

        # Add three units to the session cart.
        session = self.client.session
        session['cart'] = {str(self.product.id): 3}
        session.save()

        # Provide valid checkout details.
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

        # Act: complete the checkout request.
        self.client.post(reverse('checkout'), form_data)

        # Reload the product because its stock value was changed by the view.
        self.product.refresh_from_db()

        # Confirm that stock was reduced from 10 to 7.
        self.assertEqual(self.product.stock, 7)

    def test_checkout_stock_never_negative(self):
        """
        Confirm that stock is limited to zero when the requested quantity
        exceeds the available stock.
        """

        # Arrange: make only two units available.
        self.product.stock = 2
        self.product.save()

        # Simulate a cart requesting five units.
        session = self.client.session
        session['cart'] = {str(self.product.id): 5}
        session.save()

        # Provide valid checkout details.
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

        # Act: submit the checkout request.
        self.client.post(reverse('checkout'), form_data)

        # Reload the product to inspect its updated stock.
        self.product.refresh_from_db()

        # Confirm that stock was clamped at zero rather than becoming a
        # negative value.
        self.assertEqual(self.product.stock, 0)

    @patch('orders.views.stripe.PaymentIntent.create')
    def test_checkout_invalid_form_shows_errors(self, mock_intent):
        """
        Confirm that invalid checkout data re-renders the form with visible
        validation feedback.
        """

        # Mock Stripe so this validation test remains isolated from the
        # external payment service.
        mock_intent.return_value = type(
            'obj',
            (object,),
            {'client_secret': 'test_secret'}
        )

        # Arrange: add one product to the cart so checkout can be accessed.
        session = self.client.session
        session['cart'] = {str(self.product.id): 1}
        session.save()

        # Act: submit the form with required fields left blank.
        response = self.client.post(
            reverse('checkout'),
            {
                'full_name': '',
                'email': '',
                'address_line1': '',
                'town_city': '',
                'postcode': '',
                'country': '',
            }
        )

        # Assert: an invalid form should re-render the page rather than
        # redirecting.
        self.assertEqual(response.status_code, 200)

        # Confirm that invalid fields receive the Bootstrap error class.
        self.assertContains(response, 'is-invalid')

        # Confirm that Django's required-field validation message is shown.
        self.assertContains(response, 'This field is required')

    def test_checkout_success_page(self):
        """
        Confirm that the checkout-success page displays the completed order
        number.
        """

        # Arrange: create an order that can be retrieved by the success view.
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

        # Act: request the success page using the order number.
        response = self.client.get(
            reverse(
                'checkout_success',
                args=[order.order_number]
            )
        )

        # Assert: the page should render successfully.
        self.assertEqual(response.status_code, 200)

        # Confirm that the correct order reference appears in the response.
        self.assertContains(response, 'SUCCESS123')


class OrderHistoryTest(TestCase):
    """
    Test the authenticated order-history and order-detail views, including
    ownership restrictions and empty-state behaviour.
    """

    def setUp(self):
        """
        Create two users and one completed order before each history test.
        """

        # Import the User model locally because it is required only by this
        # group of tests.
        from django.contrib.auth.models import User

        # Create the user who owns the test order.
        self.user = User.objects.create_user(
            'historyuser',
            password='testpass123'
        )

        # Create another user for access-control tests.
        self.other = User.objects.create_user(
            'otheruser',
            password='testpass123'
        )

        # Create a product for the historical order.
        self.product = Product.objects.create(
            name='History Kettlebell',
            slug='history-kettlebell',
            description='A test product.',
            price=25.00,
            stock=10,
        )

        # Create an order belonging to the first user.
        self.order = Order.objects.create(
            order_number='HISTTEST1',
            user=self.user,
            full_name='History User',
            email='h@example.com',
            address_line1='1 Past Lane',
            town_city='Testville',
            postcode='TE5 7ST',
            country='UK',
            subtotal=25.00,
            total=25.00,
            status='delivered',
        )

        # Add one product line to the order so the history record represents
        # a realistic completed purchase.
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
            price=25.00,
        )

    def test_history_requires_login(self):
        """
        Confirm that unauthenticated users cannot access order history.
        """

        # Act: request the history page without logging in.
        response = self.client.get(reverse('order_history'))

        # Assert: Django should redirect the visitor to authentication.
        self.assertEqual(response.status_code, 302)

        # Confirm that the redirect URL points to a login page.
        self.assertIn('login', response.url)

    def test_history_lists_own_orders_only(self):
        """
        Confirm that a user can see their own orders but not orders belonging
        to another account.
        """

        # Arrange: create an order belonging to the second user.
        Order.objects.create(
            order_number='OTHERORD1',
            user=self.other,
            full_name='Other',
            email='o@example.com',
            address_line1='2 St',
            town_city='T',
            postcode='P',
            country='UK',
            subtotal=5,
            total=5,
        )

        # Log in as the owner of the original order.
        self.client.login(
            username='historyuser',
            password='testpass123'
        )

        # Act: request the order-history page.
        response = self.client.get(reverse('order_history'))

        # Assert that the logged-in user's order is displayed.
        self.assertContains(response, 'HISTTEST1')

        # Confirm that another user's order is not exposed.
        self.assertNotContains(response, 'OTHERORD1')

    def test_detail_shows_own_order(self):
        """
        Confirm that a user can open the detail page for an order they own.
        """

        # Log in as the owner of the test order.
        self.client.login(
            username='historyuser',
            password='testpass123'
        )

        # Act: request the order detail page.
        response = self.client.get(
            reverse(
                'order_detail',
                args=['HISTTEST1']
            )
        )

        # Assert that the page renders successfully.
        self.assertEqual(response.status_code, 200)

        # Confirm that delivery information from the correct order appears.
        self.assertContains(response, '1 Past Lane')

    def test_detail_ownership_guard_404(self):
        """
        Confirm that another user's order returns HTTP 404 rather than
        exposing private order information.
        """

        # Log in as a user who does not own the order.
        self.client.login(
            username='otheruser',
            password='testpass123'
        )

        # Act: attempt to access the first user's order directly.
        response = self.client.get(
            reverse(
                'order_detail',
                args=['HISTTEST1']
            )
        )

        # Assert: return 404 so the application neither displays the order
        # nor confirms that a private record exists.
        self.assertEqual(response.status_code, 404)

    def test_history_empty_state(self):
        """
        Confirm that a helpful message is displayed when a user has no
        previous orders.
        """

        # Log in as the user who has no associated orders.
        self.client.login(
            username='otheruser',
            password='testpass123'
        )

        # Act: request the order-history page.
        response = self.client.get(reverse('order_history'))

        # Assert that the template displays its empty-state message.
        self.assertContains(response, "placed any orders yet")
