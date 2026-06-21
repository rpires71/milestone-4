from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from plans.models import Plan, PlanFeature, Subscription


class PlanModelTest(TestCase):
    """Tests for the Plan, PlanFeature and Subscription models."""

    def setUp(self):
        self.plan = Plan.objects.create(
            name='Premium',
            slug='premium',
            tier='intermediate',
            price=14.99,
            status='published',
        )

    def test_plan_str(self):
        """The plan __str__ returns its name."""
        self.assertEqual(str(self.plan), 'Premium')

    def test_plan_defaults(self):
        """A plan defaults to monthly billing."""
        self.assertEqual(self.plan.billing_interval, 'monthly')

    def test_plan_feature_relationship(self):
        """Features are accessible via the plan's related name, ordered."""
        PlanFeature.objects.create(
            plan=self.plan, text='Second', display_order=2
        )
        PlanFeature.objects.create(
            plan=self.plan, text='First', display_order=1
        )
        features = list(self.plan.features.all())
        self.assertEqual(len(features), 2)
        self.assertEqual(features[0].text, 'First')

    def test_subscription_str(self):
        """The subscription __str__ includes user, plan and status."""
        user = User.objects.create_user(username='member', password='pass1234')
        sub = Subscription.objects.create(user=user, plan=self.plan)
        self.assertIn('member', str(sub))
        self.assertIn('Premium', str(sub))
        self.assertIn('active', str(sub))


class PlanViewTest(TestCase):
    """Tests for the all_plans and plan_detail views."""

    def setUp(self):
        self.published = Plan.objects.create(
            name='Published Plan',
            slug='published-plan',
            tier='beginner',
            price=4.99,
            status='published',
        )
        self.draft = Plan.objects.create(
            name='Draft Plan',
            slug='draft-plan',
            tier='beginner',
            price=4.99,
            status='draft',
        )

    def test_plans_page_loads(self):
        """The plans list page returns a 200 response."""
        response = self.client.get(reverse('plans'))
        self.assertEqual(response.status_code, 200)

    def test_plans_page_shows_published_only(self):
        """The plans list includes published plans and excludes drafts."""
        response = self.client.get(reverse('plans'))
        self.assertContains(response, 'Published Plan')
        self.assertNotContains(response, 'Draft Plan')

    def test_plan_detail_loads(self):
        """A published plan's detail page returns a 200 response."""
        response = self.client.get(
            reverse('plan_detail', args=[self.published.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Plan')

    def test_draft_plan_detail_returns_404(self):
        """A draft plan's detail page returns a 404."""
        response = self.client.get(
            reverse('plan_detail', args=[self.draft.slug])
        )
        self.assertEqual(response.status_code, 404)

    def test_invalid_slug_returns_404(self):
        """A non-existent plan slug returns a 404."""
        response = self.client.get(
            reverse('plan_detail', args=['does-not-exist'])
        )
        self.assertEqual(response.status_code, 404)