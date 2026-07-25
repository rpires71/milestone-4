"""Tests for the accounts app: profile model and signup form."""

from django.contrib.auth.models import User
from django.db import IntegrityError  # the error Django raises on a DB constraint violation
from django.test import TestCase       # base class giving each test its own throwaway database

from accounts.forms import CustomSignupForm
from accounts.models import Profile


# A test class groups related tests. Inheriting from TestCase means Django wraps
# each test method in a database transaction that's ROLLED BACK afterwards — so
# tests never pollute each other or your real data. Every test starts clean.
class ProfileModelTest(TestCase):
    """Tests for the Profile model."""

    # setUp() runs BEFORE EVERY test method in this class. It builds the fixtures
    # (test data) each test needs. Because the DB resets between tests, this fresh
    # user+profile is recreated for each one — no leftover state.
    def setUp(self):
        self.user = User.objects.create_user(
            username='member', password='pass1234'
        )
        self.profile = Profile.objects.create(user=self.user)

    # Each test method's name MUST start with "test" — that's how Django's runner
    # discovers them. The name should describe what's being checked.
    def test_profile_str(self):
        """The profile __str__ includes the username."""
        # assertEqual(a, b) passes only if a == b. Here we verify the __str__
        # method we wrote returns "member's profile", proving it works.
        self.assertEqual(str(self.profile), "member's profile")

    def test_profile_linked_to_user(self):
        """The profile is accessible via the user's related name."""
        # This proves the related_name='profile' works: from a User, user.profile
        # returns the linked Profile. Testing the relationship in both directions.
        self.assertEqual(self.user.profile, self.profile)

    def test_profile_optional_fields_blank(self):
        """Optional fields default to blank/None when not provided."""
        # setUp created a Profile with no fitness details. This confirms the
        # optional fields behave as designed: text fields default to '' (empty
        # string, from blank=True) and numeric fields to None (from null=True).
        # Note the difference — the same "null vs blank" distinction from the model.
        self.assertEqual(self.profile.fitness_goal, '')
        self.assertEqual(self.profile.experience_level, '')
        self.assertIsNone(self.profile.height_cm)
        self.assertIsNone(self.profile.weight_kg)

    def test_profile_stores_details(self):
        """A profile correctly stores fitness details when set."""
        # ARRANGE: set values on the in-memory object...
        self.profile.fitness_goal = 'muscle_gain'
        self.profile.experience_level = 'intermediate'
        self.profile.height_cm = 180
        self.profile.weight_kg = 78.50
        self.profile.save()

        # The key teaching point: we RE-FETCH from the database into a new object
        # rather than trusting the one we just edited. This proves the data truly
        # persisted to the DB, not just that our Python object holds the values.
        refreshed = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(refreshed.fitness_goal, 'muscle_gain')
        self.assertEqual(refreshed.experience_level, 'intermediate')
        self.assertEqual(refreshed.height_cm, 180)

    def test_one_profile_per_user(self):
        """The OneToOne constraint prevents a second profile for a user."""
        # This is NEGATIVE testing — proving the system correctly REJECTS bad input.
        # assertRaises is a context manager: the test passes ONLY IF the code inside
        # the "with" block raises IntegrityError. Creating a second Profile for a
        # user that already has one violates the OneToOne constraint, so the DB
        # throws IntegrityError — and catching it here proves the constraint works.
        with self.assertRaises(IntegrityError):
            Profile.objects.create(user=self.user)

    def test_signup_form_requires_and_saves_names(self):
        """The custom signup form collects first and last name onto the user."""
        # Build the form with EMPTY name fields to test validation. Forms are
        # tested by constructing them with a data dict, exactly as if submitted.
        form = CustomSignupForm(data={
            'email': 'named@example.com',
            'password1': 'a-Str0ng-passw0rd!',
            'first_name': '',   # deliberately blank...
            'last_name': '',    # ...to trigger the required-field validation
        })
        # is_valid() runs all validation. We assert it's FALSE because the names
        # are required and missing.
        self.assertFalse(form.is_valid())
        # And we check the error is specifically on first_name — proving the
        # validation failed for the RIGHT reason, not some unrelated problem.
        self.assertIn('first_name', form.errors)
