# The forms.py file defines the forms used to create and edit membership
# plans within the FitHub application. Django's ModelForm framework is
# used to generate forms directly from the Plan model, reducing duplicate
# code while allowing additional validation and presentation logic to be
# applied at the application layer.

from django import forms

# Import the model that the form will create and update.
from .models import Plan


class PlanForm(forms.ModelForm):
    """
    Provide a form for creating and editing membership plans.

    The form is intended for administrative users and applies additional
    server-side validation beyond the model where required. A single form
    supports both creating new plans and updating existing ones,
    promoting consistency and reducing code duplication.
    """

    # Provide a multi-line field for entering plan features. The content
    # is entered as plain text, with each feature placed on a separate
    # line before being processed elsewhere in the application.
    features_text = forms.CharField(
        label="Features (what's included)",
        required=False,
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text='One feature per line.',
    )

    class Meta:
        """
        Configure how the form maps to the underlying Plan model.
        """

        # Associate the form with the Plan model.
        model = Plan

        # Restrict the editable fields to those required for managing
        # membership plans.
        fields = [
            'name',
            'description',
            'tier',
            'price',
            'billing_interval',
            'status',
        ]

        # Replace default field names with clearer labels to improve the
        # usability of the administrative interface.
        labels = {
            'name': 'Plan name',
            'description': 'Description',
            'tier': 'Tier / difficulty',
            'price': 'Price (£)',
            'billing_interval': 'Billing',
            'status': 'Status',
        }

    def __init__(self, *args, **kwargs):
        """
        Customise the appearance and behaviour of the form after it has
        been created.
        """
        super().__init__(*args, **kwargs)

        # Although the database permits an empty description, the
        # application requires one so that every published plan provides
        # sufficient information for prospective customers.
        self.fields['description'].required = True

        # Define helpful placeholder text to guide users when completing
        # the form.
        placeholders = {
            'name': 'e.g. Premium',
            'description': 'Describe what members get with this plan...',
        }

        # Apply placeholders and Bootstrap styling consistently across
        # every form field. Invalid fields receive additional styling to
        # provide immediate visual feedback after validation.
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = (
                placeholders.get(field, '')
            )

            css = 'form-control'

            if self.is_bound and field in self.errors:
                css += ' is-invalid'

            self.fields[field].widget.attrs['class'] = css

    def clean_price(self):
        """
        Validate that the membership price is greater than zero before the
        form is accepted.

        Performing this validation within the form prevents invalid data
        from reaching the database and provides immediate feedback to the
        administrator.
        """
        price = self.cleaned_data.get('price')

        if price is not None and price <= 0:
            raise forms.ValidationError(
                'Price must be a positive number.'
            )

        return price
