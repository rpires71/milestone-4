from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extends the built-in User with FitHub member details."""

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

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    fitness_goal = models.CharField(
        max_length=20, choices=GOAL_CHOICES
    )
    experience_level = models.CharField(
        max_length=20, choices=EXPERIENCE_CHOICES
    )
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    weight_kg = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    profile_image = models.ImageField(
        upload_to='profiles/', null=True, blank=True
    )
    stripe_customer_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"