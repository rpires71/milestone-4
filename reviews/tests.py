# The tests.py file verifies the behaviour of the Reviews application at
# model, form and view levels. These tests confirm that reviews are stored
# correctly, ratings are validated and only authorised users can create,
# edit or delete review content.

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Import the Product model because every review must be associated with a
# specific shop product.
from shop.models import Product

# Import the form and model being tested.
from .forms import ReviewForm
from .models import Review


class ReviewModelTest(TestCase):
    """
    Test the Review model's stored values and string representation.

    Model tests confirm that review data and relationships behave as
    expected before they are used by forms, views or templates.
    """

    def setUp(self):
        """
        Create a reusable user and product before each model test.

        Django provides an isolated test database for every test, preventing
        data created in one test from affecting another.
        """
        self.user = User.objects.create_user(
            username='tester',
            password='pass1234',
        )

        self.product = Product.objects.create(
            name='Test Dumbbell',
            slug='test-dumbbell',
            description='A test product.',
            price=19.99,
        )

    def test_review_creation(self):
        """
        Confirm that a review is created with the expected rating, product
        and user relationships.
        """
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=4,
            comment='Solid product.',
        )

        self.assertEqual(review.rating, 4)
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.user, self.user)

    def test_review_str(self):
        """
        Confirm that the Review string representation contains the member,
        product and rating.

        A descriptive string improves readability in Django's
        administration interface, shell and debugging output.
        """
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
        )

        self.assertIn('tester', str(review))
        self.assertIn('Test Dumbbell', str(review))
        self.assertIn('5', str(review))


class ReviewFormTest(TestCase):
    """
    Test the ReviewForm's validation rules.

    These tests ensure that valid review data is accepted while missing or
    out-of-range ratings are rejected before reaching the database.
    """

    def test_valid_form(self):
        """
        Confirm that a rating within the permitted range and an optional
        comment produce a valid form.
        """
        form = ReviewForm(
            data={
                'rating': 4,
                'comment': 'Good.',
            }
        )

        self.assertTrue(form.is_valid())

    def test_rating_too_high_is_invalid(self):
        """
        Confirm that a rating above five is rejected by the model
        validators inherited by the ModelForm.
        """
        form = ReviewForm(
            data={
                'rating': 6,
                'comment': 'Too high.',
            }
        )

        self.assertFalse(form.is_valid())

    def test_rating_required(self):
        """
        Confirm that the form is invalid when no rating is supplied.

        Although the written comment is optional, every review must include
        a numeric rating.
        """
        form = ReviewForm(
            data={
                'comment': 'No rating given.',
            }
        )

        self.assertFalse(form.is_valid())


class ReviewViewTest(TestCase):
    """
    Test the review creation, editing and deletion views.

    These tests verify authentication, ownership checks and successful
    database changes, helping prevent users from modifying reviews that
    belong to another account.
    """

    def setUp(self):
        """
        Create two users, a product and an existing review for use across
        the view tests.
        """
        self.owner = User.objects.create_user(
            username='owner',
            password='pass1234',
        )

        self.other = User.objects.create_user(
            username='other',
            password='pass1234',
        )

        self.product = Product.objects.create(
            name='Test Bands',
            slug='test-bands',
            description='A test product.',
            price=9.99,
        )

        self.review = Review.objects.create(
            product=self.product,
            user=self.owner,
            rating=3,
            comment='Original comment.',
        )

    def test_add_review_requires_login(self):
        """
        Confirm that an anonymous visitor is redirected to the login page
        when attempting to add a review.

        Authentication is required so that every review can be linked to a
        known FitHub account.
        """
        response = self.client.get(
            reverse(
                'add_review',
                args=[self.product.slug],
            )
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_logged_in_user_can_add_review(self):
        """
        Confirm that an authenticated user can submit a new review for a
        product.
        """
        self.client.login(
            username='other',
            password='pass1234',
        )

        response = self.client.post(
            reverse(
                'add_review',
                args=[self.product.slug],
            ),
            {
                'rating': 5,
                'comment': 'Great bands.',
            },
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Review.objects.filter(
                user=self.other,
                rating=5,
            ).exists()
        )

    def test_user_cannot_edit_another_users_review(self):
        """
        Confirm that a user cannot change a review owned by another
        account.

        This protects review integrity by enforcing ownership checks in
        addition to requiring authentication.
        """
        self.client.login(
            username='other',
            password='pass1234',
        )

        response = self.client.post(
            reverse(
                'edit_review',
                args=[self.review.id],
            ),
            {
                'rating': 1,
                'comment': 'Hacked.',
            },
        )

        self.assertEqual(response.status_code, 302)

        # Reload the review so the assertions use the current database
        # values rather than the original in-memory object.
        self.review.refresh_from_db()

        self.assertEqual(self.review.rating, 3)
        self.assertEqual(
            self.review.comment,
            'Original comment.',
        )

    def test_owner_can_edit_their_review(self):
        """
        Confirm that the review owner can update their own rating and
        comment.
        """
        self.client.login(
            username='owner',
            password='pass1234',
        )

        response = self.client.post(
            reverse(
                'edit_review',
                args=[self.review.id],
            ),
            {
                'rating': 2,
                'comment': 'Updated comment.',
            },
        )

        self.assertEqual(response.status_code, 302)

        self.review.refresh_from_db()

        self.assertEqual(self.review.rating, 2)
        self.assertEqual(
            self.review.comment,
            'Updated comment.',
        )

    def test_owner_can_delete_their_review(self):
        """
        Confirm that the review owner can permanently remove their own
        review.
        """
        self.client.login(
            username='owner',
            password='pass1234',
        )

        response = self.client.post(
            reverse(
                'delete_review',
                args=[self.review.id],
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Review.objects.filter(
                id=self.review.id,
            ).exists()
        )

    def test_user_cannot_delete_another_users_review(self):
        """
        Confirm that a user cannot delete a review owned by another
        account.

        The record must remain unchanged when the ownership check fails.
        """
        self.client.login(
            username='other',
            password='pass1234',
        )

        response = self.client.post(
            reverse(
                'delete_review',
                args=[self.review.id],
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Review.objects.filter(
                id=self.review.id,
            ).exists()
        )
