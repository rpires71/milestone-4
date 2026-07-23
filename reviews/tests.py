from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from shop.models import Product
from .models import Review
from .forms import ReviewForm


class ReviewModelTest(TestCase):
    """Tests for the Review model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='tester', password='pass1234'
        )
        self.product = Product.objects.create(
            name='Test Dumbbell',
            slug='test-dumbbell',
            description='A test product.',
            price=19.99,
        )

    def test_review_creation(self):
        """A review is created with the correct field values."""
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
        """The __str__ method returns the expected format."""
        review = Review.objects.create(
            product=self.product, user=self.user, rating=5
        )
        self.assertIn('tester', str(review))
        self.assertIn('Test Dumbbell', str(review))
        self.assertIn('5', str(review))


class ReviewFormTest(TestCase):
    """Tests for the ReviewForm validation."""

    def test_valid_form(self):
        """A rating within 1-5 with a comment is valid."""
        form = ReviewForm(data={'rating': 4, 'comment': 'Good.'})
        self.assertTrue(form.is_valid())

    def test_rating_too_high_is_invalid(self):
        """A rating above 5 is rejected by the model validators."""
        form = ReviewForm(data={'rating': 6, 'comment': 'Too high.'})
        self.assertFalse(form.is_valid())

    def test_rating_required(self):
        """A missing rating makes the form invalid."""
        form = ReviewForm(data={'comment': 'No rating given.'})
        self.assertFalse(form.is_valid())


class ReviewViewTest(TestCase):
    """Tests for the review add/edit/delete views."""

    def setUp(self):
        self.owner = User.objects.create_user(
            username='owner', password='pass1234'
        )
        self.other = User.objects.create_user(
            username='other', password='pass1234'
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
        """An anonymous user is redirected to login when adding a review."""
        response = self.client.get(
            reverse('add_review', args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_logged_in_user_can_add_review(self):
        """A logged-in user can post a new review."""
        self.client.login(username='other', password='pass1234')
        response = self.client.post(
            reverse('add_review', args=[self.product.slug]),
            {'rating': 5, 'comment': 'Great bands.'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Review.objects.filter(user=self.other, rating=5).exists()
        )

    def test_user_cannot_edit_another_users_review(self):
        """A user editing someone else's review is redirected without change."""
        self.client.login(username='other', password='pass1234')
        response = self.client.post(
            reverse('edit_review', args=[self.review.id]),
            {'rating': 1, 'comment': 'Hacked.'},
        )
        self.assertEqual(response.status_code, 302)
        self.review.refresh_from_db()
        self.assertEqual(self.review.rating, 3)
        self.assertEqual(self.review.comment, 'Original comment.')

    def test_owner_can_edit_their_review(self):
        """The review owner can update their own review."""
        self.client.login(username='owner', password='pass1234')
        response = self.client.post(
            reverse('edit_review', args=[self.review.id]),
            {'rating': 2, 'comment': 'Updated comment.'},
        )
        self.assertEqual(response.status_code, 302)
        self.review.refresh_from_db()
        self.assertEqual(self.review.rating, 2)
        self.assertEqual(self.review.comment, 'Updated comment.')

    def test_owner_can_delete_their_review(self):
        """The review owner can delete their own review."""
        self.client.login(username='owner', password='pass1234')
        response = self.client.post(
            reverse('delete_review', args=[self.review.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())

    def test_user_cannot_delete_another_users_review(self):
        """A user cannot delete a review they do not own."""
        self.client.login(username='other', password='pass1234')
        response = self.client.post(
            reverse('delete_review', args=[self.review.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Review.objects.filter(id=self.review.id).exists())
