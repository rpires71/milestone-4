from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone', 'address_line1',
                  'address_line2', 'town_city', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        """Add Bootstrap classes and placeholders to fields."""
        super().__init__(*args, **kwargs)
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
        for field in self.fields:
            placeholder = placeholders.get(field, '')
            self.fields[field].widget.attrs['placeholder'] = placeholder
            css = 'form-control'
            # Highlight invalid fields with Bootstrap's is-invalid class
            if self.is_bound and field in self.errors:
                css += ' is-invalid'
            self.fields[field].widget.attrs['class'] = css
            self.fields[field].label = labels.get(field, field)
