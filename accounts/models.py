"""Models for user profiles and fitness details."""

# We import Django's built-in User rather than defining our own. FitHub extends
# User with extra fields instead of replacing it — the standard, low-risk way to
# add profile data without touching Django's authentication machinery.
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Extends the built-in User with FitHub member details."""

    # CHOICES define a fixed set of allowed values for a field. Each tuple is
    # (stored_value, human_label): the left side is saved in the database, the
    # right side is what's shown in forms and the admin. Defining them as class
    # attributes lets both this model AND the form (which imports GOAL_CHOICES)
    # share one source of truth.
    GOAL_CHOICES = [
        ('weight_loss', 'Weight loss'),
        ('muscle_gain', 'Muscle gain'),
        ('general_fitness', 'General fitness'),
        ('endurance', 'Endurance'),
        ('flexibility', 'Flexibility'),
    ]
    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    # OneToOneField = exactly one Profile per User (and vice versa). This is the
    # "extend User" pattern.
    #   on_delete=CASCADE: if the User is deleted, delete their Profile too.
    #   related_name='profile': lets you write user.profile to reach this object
    #   from the User side (the reverse of the relationship).
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    # CharField = short text, with a required max_length. choices restricts input
    # to the tuples above, so the DB can only hold one of those five values.
    fitness_goal = models.CharField(
        max_length=20, choices=GOAL_CHOICES
    )
    experience_level = models.CharField(
        max_length=20, choices=EXPERIENCE_CHOICES
    )
    # PositiveIntegerField = whole numbers >= 0. null/blank make it OPTIONAL:
    #   null=True  -> the database column may store NULL (no value)
    #   blank=True -> forms allow it to be left empty
    # You almost always need BOTH for an optional field: null is the database
    # layer, blank is the form/validation layer.
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    # DecimalField for weight because money and measurements need exact precision
    # (floats can round oddly). max_digits=5, decimal_places=2 allows values like
    # 123.45 (5 digits total, 2 after the point).
    weight_kg = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    # ImageField stores a path to an uploaded file; upload_to sets the subfolder.
    # NOTE: this needs MEDIA storage configured to actually work, and Heroku's
    # filesystem is ephemeral — which is why image upload is listed as future
    # work rather than a delivered feature.
    profile_image = models.ImageField(
        upload_to='profiles/', null=True, blank=True
    )
    # Stores the member's Stripe customer reference so billing links to the
    # right Stripe record. blank=True (but not null=True) means the form can
    # leave it empty and it's stored as an empty string "" rather than NULL —
    # the common convention for optional text fields.
    stripe_customer_id = models.CharField(max_length=255, blank=True)
    # auto_now_add sets the timestamp ONCE, when the row is first created.
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now updates the timestamp EVERY time the row is saved. Together these
    # give you "when created" and "when last changed" for free.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # __str__ controls how this object appears as text — in the admin, in
        # the shell, in debugging. Without it you'd see "Profile object (1)";
        # with it you see "alice's profile", which is far more useful.
        return f"{self.user.username}'s profile"
