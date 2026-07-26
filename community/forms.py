"""Form for creating and editing community posts."""

from django import forms

from .models import Post


# A ModelForm builds its fields automatically from a model â€” no need to declare
# each field by hand. Compare this to accounts' CustomSignupForm, which declared
# fields explicitly; here the fields come straight from the Post model.
class PostForm(forms.ModelForm):
    """Form for a community post, generating fields from the Post model."""

    # The inner Meta class tells the ModelForm which model to build from and
    # which of its fields to include.
    class Meta:
        model = Post
        # Only these two fields appear on the form. Post also has author,
        # created_at, and updated_at â€” but those are set automatically (author
        # in the view, timestamps by the model), so they're deliberately
        # excluded from user input.
        fields = ['title', 'content']
        # widgets overrides the default HTML control for each field, adding
        # Bootstrap's form-control class (and, for content, 5 rows of height).
        # This styles the inputs without needing widget_tweaks in the template.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }
