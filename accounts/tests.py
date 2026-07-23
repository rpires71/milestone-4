from django.test import TestCase
from django.contrib.auth.models import User

from accounts.forms import CustomSignupForm
from accounts.models import Profile


class ProfileModelTest(TestCase):
    """Tests for the Profile model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='member', password='pass1234'
        )
        self.profile = Profile.objects.create(user=self.user)

    def test_profile_str(self):
        """The profile __str__ includes the username."""
        self.assertEqual(str(self.profile), "member's profile")

    def test_profile_linked_to_user(self):
        """The profile is accessible via the user's related name."""
        self.assertEqual(self.user.profile, self.profile)

    def test_profile_optional_fields_blank(self):
        """Optional fields default to blank/None when not provided."""
        self.assertEqual(self.profile.fitness_goal, '')
        self.assertEqual(self.profile.experience_level, '')
        self.assertIsNone(self.profile.height_cm)
        self.assertIsNone(self.profile.weight_kg)

    def test_profile_stores_details(self):
        """A profile correctly stores fitness details when set."""
        self.profile.fitness_goal = 'muscle_gain'
        self.profile.experience_level = 'intermediate'
        self.profile.height_cm = 180
        self.profile.weight_kg = 78.50
        self.profile.save()

        refreshed = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(refreshed.fitness_goal, 'muscle_gain')
        self.assertEqual(refreshed.experience_level, 'intermediate')
        self.assertEqual(refreshed.height_cm, 180)

    def test_one_profile_per_user(self):
        """The OneToOne constraint prevents a second profile for a user."""
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Profile.objects.create(user=self.user)

    def test_signup_form_requires_and_saves_names(self):
        """The custom signup form collects first and last name onto the user."""
        form = CustomSignupForm(data={
            'email': 'named@example.com',
            'password1': 'a-Str0ng-passw0rd!',
            'first_name': '',
            'last_name': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
