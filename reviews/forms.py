# The forms.py file defines the form used to collect customer reviews.
# Django's ModelForm framework generates the form directly from the
# Review model while allowing the application's presentation and user
# experience to be customised without duplicating model definitions.

from django import forms

# Import the model that the form will create and validate.
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Provide a form that allows authenticated users to submit a product
    or service review.

    The form exposes only the fields that users should complete while
    applying Bootstrap styling to provide a consistent appearance across
    the FitHub application.
    """

    class Meta:
        """
        Configure how the form maps to the underlying Review model.
        """

        # Associate the form with the Review model.
        model = Review

        # Restrict the editable fields to those required when submitting a
        # customer review.
        fields = [
            'rating',
            'comment',
        ]

        # Apply Bootstrap styling and HTML input constraints to improve
        # usability while complementing the application's server-side
        # validation.
        widgets = {
            'rating': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 5,
                    'class': 'form-control',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'rows': 3,
                    'class': 'form-control',
                }
            ),
        }
