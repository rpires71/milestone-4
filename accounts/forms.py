"""Forms for user signup and profile editing."""

from django import forms
from allauth.account.forms import SignupForm

from .models import Profile


class CustomSignupForm(SignupForm):
    """Extend allauth's signup form to collect the user's name.

    The extra fields render automatically on the existing signup page via the
    shared allauth form element template, and save() stamps them onto the
    Django User's built-in first_name / last_name fields.
    """

    first_name = forms.CharField(
        max_length=150,
        label="First name",
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )
    last_name = forms.CharField(
        max_length=150,
        label="Surname",
        widget=forms.TextInput(attrs={"placeholder": "Surname"}),
    )

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user


class FitnessProfileForm(forms.ModelForm):
    """Form for editing a user's fitness profile."""

    class Meta:
        model = Profile
        fields = [
            "fitness_goal",
            "experience_level",
            "height_cm",
            "weight_kg",
        ]

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # These are CharField-with-choices (not ModelChoiceField), so the blank
        # option comes from the model's blank=True. Override choices to drop it.
        self.fields["fitness_goal"].choices = Profile.GOAL_CHOICES
        self.fields["experience_level"].choices = Profile.EXPERIENCE_CHOICES

        # Required for the two-step registration; height/weight stay optional.
        self.fields["fitness_goal"].required = True
        self.fields["experience_level"].required = True
