from django import forms

from .models import Plan


class PlanForm(forms.ModelForm):
    """Create/edit form for membership plans (staff only).

    All validation is performed server-side. The same form is used for both
    create and update, matching the shared-form design in the wireframe.
    """

    features_text = forms.CharField(
        label="Features (what's included)",
        required=False,
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text='One feature per line.',
    )

    class Meta:
        model = Plan
        fields = ['name', 'description', 'tier', 'price', 'billing_interval', 'status']
        labels = {
            'name': 'Plan name',
            'description': 'Description',
            'tier': 'Tier / difficulty',
            'price': 'Price (£)',
            'billing_interval': 'Billing',
            'status': 'Status',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Description is required for a sellable plan, even though the model
        # allows blank (server-side rule, per the wireframe).
        self.fields['description'].required = True
        placeholders = {
            'name': 'e.g. Premium',
            'description': 'Describe what members get with this plan...',
        }
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders.get(field, '')
            css = 'form-control'
            if self.is_bound and field in self.errors:
                css += ' is-invalid'
            self.fields[field].widget.attrs['class'] = css

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError('Price must be a positive number.')
        return price