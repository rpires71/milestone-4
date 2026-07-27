# The models.py file defines the database structure for customer reviews.
# Each review links an authenticated member to a product, allowing users
# to submit a rating and optional written feedback. Validation rules and
# model relationships help maintain data integrity while supporting the
# product review functionality within FitHub.

from django.contrib.auth.models import User

# Import validators used to restrict review ratings to an acceptable
# range before the data is saved.
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

# Import the Product model so that reviews can be associated with
# individual products available within the shop.
from shop.models import Product


class Review(models.Model):
    """
    Represent a member's rating and written review of a product.

    Each review is linked to both a user and a product, allowing customer
    feedback to be displayed alongside products while ensuring each
    member can submit only one review per product.
    """

    # Associate the review with the product being evaluated. Deleting a
    # product automatically removes its related reviews.
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    # Associate the review with the authenticated member who submitted
    # it. Removing a user also removes their reviews.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    # Store the review rating. Validators ensure that only whole-number
    # ratings between one and five are accepted.
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    # Allow members to provide optional written feedback in addition to
    # the numeric rating.
    comment = models.TextField(blank=True)

    # Automatically record when the review was first submitted.
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically record when the review was last modified.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Configure additional database behaviour for the Review model.
        """

        # Prevent the same user from submitting multiple reviews for the
        # same product, helping maintain fair and consistent ratings.
        unique_together = ('user', 'product')

    def __str__(self):
        """
        Return a readable representation of the review for use throughout
        the Django administration interface and debugging tools.
        """
        return (
            f"{self.user.username} – "
            f"{self.product.name} ({self.rating}★)"
        )
