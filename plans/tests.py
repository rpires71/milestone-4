from unittest.mock import patch, Mock
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Plan, Subscription, PlanFeature


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


class SubscribeViewTests(TestCase):
    """Tests for the subscribe view (starts a Stripe subscription checkout)."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='bob', email='bob@example.com', password='pass12345'
        )
        # A published plan WITH a Stripe price id (subscribable)
        self.plan = Plan.objects.create(
            name='Pro', slug='pro', tier='advanced',
            price=Decimal('9.99'), status='published',
            stripe_price_id='price_test123',
        )
        # A published plan WITHOUT a price id (not subscribable yet)
        self.plan_no_price = Plan.objects.create(
            name='Basic', slug='basic', tier='beginner',
            price=Decimal('4.99'), status='published',
            stripe_price_id='',
        )

    def test_subscribe_requires_login(self):
        """Anonymous users are redirected to login."""
        response = self.client.get(reverse('subscribe', args=[self.plan.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    @patch('plans.views.stripe.checkout.Session.create')
    def test_subscribe_creates_stripe_session_and_redirects(self, mock_create):
        """A logged-in user subscribing is sent to the Stripe checkout URL."""
        mock_create.return_value = Mock(url='https://checkout.stripe.com/c/test')
        self.client.login(username='bob', password='pass12345')

        response = self.client.get(reverse('subscribe', args=[self.plan.slug]))

        # Stripe was called once
        self.assertTrue(mock_create.called)
        # ...in subscription mode, with this plan's price id
        kwargs = mock_create.call_args.kwargs
        self.assertEqual(kwargs['mode'], 'subscription')
        self.assertEqual(kwargs['line_items'][0]['price'], 'price_test123')
        # ...and we redirect to the URL Stripe returned
        self.assertIn(response.status_code, (302, 303))
        self.assertEqual(response.url, 'https://checkout.stripe.com/c/test')

    @patch('plans.views.stripe.checkout.Session.create')
    def test_subscribe_without_price_id_does_not_call_stripe(self, mock_create):
        """A plan with no stripe_price_id errors and never hits Stripe."""
        self.client.login(username='bob', password='pass12345')

        response = self.client.get(
            reverse('subscribe', args=[self.plan_no_price.slug])
        )

        self.assertFalse(mock_create.called)
        self.assertEqual(response.status_code, 302)  # redirected back to plan detail

    def test_subscribe_unpublished_plan_404(self):
        """Draft/archived plans cannot be subscribed to."""
        draft = Plan.objects.create(
            name='Hidden', slug='hidden', tier='intermediate',
            price=Decimal('1.99'), status='draft',
            stripe_price_id='price_x',
        )
        self.client.login(username='bob', password='pass12345')
        response = self.client.get(reverse('subscribe', args=[draft.slug]))
        self.assertEqual(response.status_code, 404)


class SubscriptionSuccessViewTests(TestCase):
    """Tests for the subscription_success view (records the Subscription)."""

    def setUp(self):
        self.user = User.objects.create_user(
            username='bob', email='bob@example.com', password='pass12345'
        )
        self.plan = Plan.objects.create(
            name='Pro', slug='pro', tier='advanced',
            price=Decimal('9.99'), status='published',
            stripe_price_id='price_test123',
        )
        self.url = reverse('subscription_success')

    def test_success_requires_login(self):
        response = self.client.get(self.url, {'plan': self.plan.slug})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_success_creates_subscription(self):
        """Hitting the success page records a Subscription for the user."""
        self.client.login(username='bob', password='pass12345')
        response = self.client.get(self.url, {'plan': self.plan.slug})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Subscription.objects.filter(user=self.user, plan=self.plan).exists()
        )

    def test_success_is_idempotent(self):
        """Visiting success twice does not create duplicate subscriptions."""
        self.client.login(username='bob', password='pass12345')
        self.client.get(self.url, {'plan': self.plan.slug})
        self.client.get(self.url, {'plan': self.plan.slug})

        count = Subscription.objects.filter(
            user=self.user, plan=self.plan
        ).count()
        self.assertEqual(count, 1)


class PlanManagementTest(TestCase):
    """Tests for the staff-only plan management CRUD."""

    def setUp(self):
        from django.contrib.auth.models import User
        self.staff = User.objects.create_user(
            'staffmember', password='testpass123', is_staff=True
        )
        self.member = User.objects.create_user(
            'regularmember', password='testpass123'
        )
        self.plan = Plan.objects.create(
            name='Manage Me', slug='manage-me', tier='beginner',
            price=9.99, status='published',
        )

    def test_non_staff_gets_403(self):
        """Direct URL access by non-staff (and anonymous) returns 403."""
        urls = [
            reverse('manage_plans'),
            reverse('plan_create'),
            reverse('plan_edit', args=['manage-me']),
            reverse('plan_archive', args=['manage-me']),
        ]
        for url in urls:
            self.assertEqual(self.client.get(url).status_code, 403)
        self.client.login(username='regularmember', password='testpass123')
        for url in urls:
            self.assertEqual(self.client.get(url).status_code, 403)

    def test_staff_sees_all_statuses(self):
        Plan.objects.create(
            name='Hidden Draft', slug='hidden-draft', tier='beginner',
            price=5, status='draft',
        )
        self.client.login(username='staffmember', password='testpass123')
        response = self.client.get(reverse('manage_plans'))
        self.assertContains(response, 'Hidden Draft')
        self.assertContains(response, 'Manage Me')

    def test_staff_can_create_plan_with_features(self):
        self.client.login(username='staffmember', password='testpass123')
        response = self.client.post(reverse('plan_create'), {
            'name': 'Created Plan', 'description': 'A new plan.',
            'tier': 'advanced', 'price': '19.99',
            'billing_interval': 'monthly', 'status': 'published',
            'features_text': 'First feature\nSecond feature',
        })
        self.assertEqual(response.status_code, 302)
        plan = Plan.objects.get(name='Created Plan')
        self.assertEqual(plan.slug, 'created-plan')
        self.assertEqual(plan.features.count(), 2)

    def test_negative_price_rejected(self):
        self.client.login(username='staffmember', password='testpass123')
        response = self.client.post(reverse('plan_create'), {
            'name': 'Bad Price', 'description': 'x', 'tier': 'beginner',
            'price': '-5', 'billing_interval': 'monthly', 'status': 'draft',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'positive number')
        self.assertFalse(Plan.objects.filter(name='Bad Price').exists())

    def test_staff_can_edit_plan(self):
        self.client.login(username='staffmember', password='testpass123')
        response = self.client.post(
            reverse('plan_edit', args=['manage-me']),
            {
                'name': 'Manage Me', 'description': 'Updated description.',
                'tier': 'intermediate', 'price': '14.99',
                'billing_interval': 'monthly', 'status': 'published',
                'features_text': 'Updated feature',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.plan.refresh_from_db()
        self.assertEqual(self.plan.tier, 'intermediate')
        self.assertEqual(self.plan.features.count(), 1)

    def test_archive_is_soft_delete(self):
        """Archiving sets status rather than deleting the row."""
        self.client.login(username='staffmember', password='testpass123')
        response = self.client.post(reverse('plan_archive', args=['manage-me']))
        self.assertEqual(response.status_code, 302)
        self.plan.refresh_from_db()
        self.assertEqual(self.plan.status, 'archived')

    def test_archived_plan_hidden_from_public(self):
        self.plan.status = 'archived'
        self.plan.save()
        response = self.client.get(reverse('plans'))
        self.assertNotContains(response, 'Manage Me')