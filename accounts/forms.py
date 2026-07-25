"""Forms for user signup and profile editing."""

from allauth.account.forms import SignupForm
from django import forms

from .models import Profile


# allauth provides its own SignupForm. Rather than replace it, we SUBCLASS it,
# so we inherit all of allauth's email/password handling and only add what we
# need (the user's name). This is the "extend, don't rebuild" principle.
class CustomSignupForm(SignupForm):
    """Extend allauth's signup form to collect the user's name.

    The extra fields render automatically on the existing signup page via the
    shared allauth form element template, and save() stamps them onto the
    Django User's built-in first_name / last_name fields.
    """
    # Declaring fields as class attributes adds them to the form. Because this
    # class inherits from SignupForm, these appear ALONGSIDE allauth's existing
    # email/password fields, not instead of them.
    first_name = forms.CharField(
        max_length=150,
        label="First name",
        # The widget controls the HTML <input> that renders. attrs become
        # HTML attributes, so this adds placeholder="First name" to the input.
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )
    last_name = forms.CharField(
        max_length=150,
        label="Surname",
        widget=forms.TextInput(attrs={"placeholder": "Surname"}),
    )

    def save(self, request):
        # super().save() runs allauth's original save first — it creates the
        # User and handles the password. We capture the returned user object...
        user = super().save(request)
        # ...then set our extra fields on it. cleaned_data holds the validated
        # form input, so these values have already passed field validation.
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        # A second .save() writes the two new fields to the database. (allauth's
        # save already created the row; this updates it.)
        user.save()
        return user


class FitnessProfileForm(forms.ModelForm):
    """Form for editing a user's fitness profile."""

    # A ModelForm builds its fields automatically FROM a model. The inner Meta
    # class tells Django which model and which fields to include — so we don't
    # redeclare each field by hand the way CustomSignupForm did above.
    class Meta:
        model = Profile
        # Only these four Profile fields appear on the form. Any other model
        # fields (e.g. the Stripe customer id) are deliberately excluded.
        fields = [
            "fitness_goal",
            "experience_level",
            "height_cm",
            "weight_kg",
        ]

        # widgets overrides the default HTML control for a field. Here we swap
        # dropdowns for radio buttons, and add Bootstrap classes plus min/max/
        # step constraints so the browser enforces sensible numeric ranges.
        widgets = {
            "fitness_goal": forms.RadioSelect(attrs={"class": "form-check-input"}),
            "experience_level": forms.RadioSelect(attrs={"class": "form-check-input"}),
            "height_cm": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "100",
                "max": "250",
                "step": "1",
            }),
            "weight_kg": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "30",
                "max": "250",
                "step": "0.1",
            }),
        }

    # __init__ runs every time a form instance is created. Overriding it lets us
    # adjust fields at runtime — things that can't be expressed in Meta alone.
    def __init__(self, *args, **kwargs):
        # Always call super().__init__ first so Django builds the fields from
        # Meta before we start modifying them.
        super().__init__(*args, **kwargs)

        # These are CharField-with-choices (not ModelChoiceField), so the blank
        # option comes from the model's blank=True. Override choices to drop it.
        self.fields["fitness_goal"].choices = Profile.GOAL_CHOICES
        self.fields["experience_level"].choices = Profile.EXPERIENCE_CHOICES

        # Required for the two-step registration; height/weight stay optional.
        self.fields["fitness_goal"].required = True
        self.fields["experience_level"].required = True
