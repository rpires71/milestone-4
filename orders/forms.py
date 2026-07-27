# The forms.py file defines the forms used by the Orders application.
# Django forms provide a structured and secure way of collecting,
# validating and processing user input before it is stored in the
# database. In this application, the checkout form captures the
# customer's delivery information required to complete an order.

"""Forms for capturing delivery details at checkout."""

from django import forms

# Import the Order model so that the form can automatically generate
# fields that correspond to the model's database structure.
from .models import Order


class OrderForm(forms.ModelForm):
    """
    ModelForm used to collect and validate the customer's delivery
    information during the checkout process.
    """

    class Meta:
        """
        Define the model associated with the form and specify which
        database fields should be displayed to the user.
        """

        # Associate this form with the Order model.
        model = Order

        # Include only the fields required to capture delivery details
        # during checkout.
        fields = (
            'full_name',
            'email',
            'phone',
            'address_line1',
            'address_line2',
            'town_city',
            'postcode',
            'country',
        )

    def __init__(self, *args, **kwargs):
        """
        Customise the appearance of the generated form by applying
        Bootstrap styling, descriptive placeholders and user-friendly
        field labels.
        """

        # Initialise the parent ModelForm before applying any
        # customisations.
        super().__init__(*args, **kwargs)

        # Define placeholder text to provide users with guidance about
        # the information expected in each field.
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'town_city': 'Town or City',
            'postcode': 'Postal Code',
            'country': 'Country',
        }

        # Define descriptive labels that improve the readability and
        # accessibility of the checkout form.
        labels = {
            'full_name': 'Full name',
            'email': 'Email address',
            'phone': 'Phone (optional)',
            'address_line1': 'Address line 1',
            'address_line2': 'Address line 2 (optional)',
            'town_city': 'Town / City',
            'postcode': 'Postcode',
            'country': 'Country',
        }

        # Iterate through each generated form field and apply
        # consistent styling and user interface enhancements.
        for field in self.fields:

            # Retrieve the placeholder associated with the current
            # field, using an empty string if none is defined.
            placeholder = placeholders.get(field, '')

            # Apply the placeholder text to the HTML input element.
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Apply Bootstrap's standard form styling.
            css = 'form-control'

            # If the submitted form contains validation errors,
            # highlight the affected field using Bootstrap's
            # 'is-invalid' class to improve user feedback.
            if self.is_bound and field in self.errors:
                css += ' is-invalid'

            # Apply the final CSS classes to the field.
            self.fields[field].widget.attrs['class'] = css

            # Replace the default field label with a more
            # user-friendly description.
            self.fields[field].label = labels.get(field, field)
