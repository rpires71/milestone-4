from django import forms
from .models import Profile


class FitnessProfileForm(forms.ModelForm):
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