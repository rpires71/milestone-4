# The tests.py file verifies the behaviour of the Plans application at
# model, view, payment-integration and administration levels. These tests
# help ensure that membership plans are displayed correctly, Stripe
# subscription checkout is handled securely, subscriptions are recorded
# only after verified payment and plan-management functions remain
# restricted to authorised staff members.

from decimal import Decimal

# Mock and patch allow Stripe API calls to be replaced with controlled
# test objects. This keeps the automated suite independent of Stripe's
# external service and prevents real checkout sessions from being created.
from unittest.mock import Mock, patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Import the models used to create isolated test data and verify changes
# made by the Plans application's views.
from .models import Plan, PlanFeature, Subscription


class PlanModelTest(TestCase):
    """
    Test the behaviour and relationships of the Plan, PlanFeature and
    Subscription models.

    Model tests confirm that defaults, string representations and related
    objects behave consistently before those models are used by views,
    templates or administrative workflows.
    """

    def setUp(self):
        """
        Create a reusable published plan before each model test.

        Django provides every test with an isolated test database, so
        changes made by one test cannot affect the outcome of another.
        """
        self.plan = Plan.objects.create(
            name='Premium',
            slug='premium',
            tier='intermediate',
            price=14.99,
            status='published',
        )

    def test_plan_str(self):
        """
        Confirm that the Plan string representation returns its name.

        A meaningful string representation improves readability in the
        Django administration interface, shell and debugging output.
        """
        self.assertEqual(str(self.plan), 'Premium')

    def test_plan_defaults(self):
        """
        Confirm that a new plan uses monthly billing by default.

        This protects the model's intended default behaviour when no
        billing interval is supplied during object creation.
        """
        self.assertEqual(self.plan.billing_interval, 'monthly')

    def test_plan_feature_relationship(self):
        """
        Confirm that related features are accessible through the plan and
        returned in their configured display order.
        """

        # Create the feature with the later display position first to
        # demonstrate that database insertion order does not control the
        # final presentation order.
        PlanFeature.objects.create(
            plan=self.plan,
            text='Second',
            display_order=2,
        )

        PlanFeature.objects.create(
            plan=self.plan,
            text='First',
            display_order=1,
        )

        # Access the features through the related_name defined on the
        # PlanFeature foreign key.
        features = list(self.plan.features.all())

        self.assertEqual(len(features), 2)

        # The model's Meta ordering should place the feature with the
        # lowest display_order value first.
        self.assertEqual(features[0].text, 'First')

    def test_subscription_str(self):
        """
        Confirm that the Subscription string representation contains the
        member, plan and current subscription status.
        """
        user = User.objects.create_user(
            username='member',
            password='pass1234',
        )

        subscription = Subscription.objects.create(
            user=user,
            plan=self.plan,
        )

        self.assertIn('member', str(subscription))
        self.assertIn('Premium', str(subscription))
        self.assertIn('active', str(subscription))


class PlanViewTest(TestCase):
    """
    Test the public plan-list and plan-detail views.

    These tests confirm that visitors can view published plans while draft
    or invalid plans remain inaccessible through public-facing URLs.
    """

    def setUp(self):
        """
        Create published and draft plans so that visibility rules can be
        tested against different plan states.
        """
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
        """
        Confirm that the public plans page responds successfully.
        """
        response = self.client.get(reverse('plans'))

        self.assertEqual(response.status_code, 200)

    def test_plans_page_shows_published_only(self):
        """
        Confirm that the public list displays published plans but excludes
        plans that are still in draft form.
        """
        response = self.client.get(reverse('plans'))

        self.assertContains(response, 'Published Plan')
        self.assertNotContains(response, 'Draft Plan')

    def test_plan_detail_loads(self):
        """
        Confirm that the detail page for a published plan is available and
        contains the expected plan information.
        """
        response = self.client.get(
            reverse(
                'plan_detail',
                args=[self.published.slug],
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Plan')

    def test_draft_plan_detail_returns_404(self):
        """
        Confirm that a draft plan cannot be accessed through its public
        detail URL.

        Returning HTTP 404 avoids exposing unpublished products to
        customers before they are ready for release.
        """
        response = self.client.get(
            reverse(
                'plan_detail',
                args=[self.draft.slug],
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_invalid_slug_returns_404(self):
        """
        Confirm that an unknown plan slug produces a standard 404 response
        instead of an unhandled application error.
        """
        response = self.client.get(
            reverse(
                'plan_detail',
                args=['does-not-exist'],
            )
        )

        self.assertEqual(response.status_code, 404)


class SubscribeViewTests(TestCase):
    """
    Test the view that starts a Stripe subscription checkout session.

    The tests verify authentication, request-method restrictions, plan
    publication status, Stripe configuration and redirection to the
    checkout URL supplied by Stripe.
    """

    def setUp(self):
        """
        Create a member and two published plans representing valid and
        incomplete Stripe configurations.
        """
        self.user = User.objects.create_user(
            username='bob',
            email='bob@example.com',
            password='pass12345',
        )

        # This plan contains a Stripe Price identifier and can therefore
        # be used to create a recurring subscription checkout session.
        self.plan = Plan.objects.create(
            name='Pro',
            slug='pro',
            tier='advanced',
            price=Decimal('9.99'),
            status='published',
            stripe_price_id='price_test123',
        )

        # This plan is published but has not yet been linked to a Stripe
        # Price, so checkout must not be attempted.
        self.plan_no_price = Plan.objects.create(
            name='Basic',
            slug='basic',
            tier='beginner',
            price=Decimal('4.99'),
            status='published',
            stripe_price_id='',
        )

    def test_subscribe_requires_login(self):
        """
        Confirm that anonymous visitors are redirected to the login page.

        Requiring authentication ensures that a future subscription can be
        associated with a known FitHub account.
        """
        response = self.client.get(
            reverse(
                'subscribe',
                args=[self.plan.slug],
            )
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    @patch('plans.views.stripe.checkout.Session.create')
    def test_subscribe_creates_stripe_session_and_redirects(
        self,
        mock_create,
    ):
        """
        Confirm that an authenticated subscription request creates a
        Stripe Checkout Session and redirects the member to Stripe.

        Stripe is mocked so that the test can verify the application's API
        arguments without contacting the live payment service.
        """

        # Simulate the limited part of Stripe's response used by the view.
        mock_create.return_value = Mock(
            url='https://checkout.stripe.com/c/test'
        )

        self.client.login(
            username='bob',
            password='pass12345',
        )

        response = self.client.post(
            reverse(
                'subscribe',
                args=[self.plan.slug],
            )
        )

        # Confirm that the Stripe checkout function was invoked.
        self.assertTrue(mock_create.called)

        # Inspect the keyword arguments supplied to Stripe to confirm that
        # the request uses recurring subscription mode and the correct
        # Stripe Price identifier.
        kwargs = mock_create.call_args.kwargs

        self.assertEqual(
            kwargs['mode'],
            'subscription',
        )
        self.assertEqual(
            kwargs['line_items'][0]['price'],
            'price_test123',
        )

        # Stripe-related redirects may use either 302 or 303 depending on
        # the response implementation, so both valid redirect statuses are
        # accepted.
        self.assertIn(
            response.status_code,
            (302, 303),
        )
        self.assertEqual(
            response.url,
            'https://checkout.stripe.com/c/test',
        )

    @patch('plans.views.stripe.checkout.Session.create')
    def test_subscribe_without_price_id_does_not_call_stripe(
        self,
        mock_create,
    ):
        """
        Confirm that a plan without a Stripe Price identifier does not
        start an external checkout session.

        This defensive check prevents incomplete plan data from causing an
        invalid or misleading payment request.
        """
        self.client.login(
            username='bob',
            password='pass12345',
        )

        response = self.client.post(
            reverse(
                'subscribe',
                args=[self.plan_no_price.slug],
            )
        )

        # Stripe must not be contacted when the required identifier is
        # missing.
        self.assertFalse(mock_create.called)

        # The member is redirected back to an internal page where an
        # explanatory Django message can be displayed.
        self.assertEqual(response.status_code, 302)

    def test_subscribe_unpublished_plan_404(self):
        """
        Confirm that draft or archived plans cannot be purchased.
        """
        draft = Plan.objects.create(
            name='Hidden',
            slug='hidden',
            tier='intermediate',
            price=Decimal('1.99'),
            status='draft',
            stripe_price_id='price_x',
        )

        self.client.login(
            username='bob',
            password='pass12345',
        )

        response = self.client.post(
            reverse(
                'subscribe',
                args=[draft.slug],
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_subscribe_get_request_rejected(self):
        """
        Confirm that subscription creation rejects GET requests.

        Requiring POST prevents a payment action from being initiated by
        merely visiting a URL, following a link or loading a cached page.
        """
        self.client.login(
            username='bob',
            password='pass12345',
        )

        response = self.client.get(
            reverse(
                'subscribe',
                args=[self.plan.slug],
            )
        )

        self.assertEqual(response.status_code, 405)


class SubscriptionSuccessViewTests(TestCase):
    """
    Test the subscription-success view that verifies Stripe checkout and
    creates or updates the local Subscription record.

    These tests ensure that the application does not trust query-string
    data alone and records a subscription only after the Stripe session
    has been retrieved and confirmed as paid.
    """

    def setUp(self):
        """
        Create a user, a subscribable plan and the success URL used
        throughout this group of tests.
        """
        self.user = User.objects.create_user(
            username='bob',
            email='bob@example.com',
            password='pass12345',
        )

        self.plan = Plan.objects.create(
            name='Pro',
            slug='pro',
            tier='advanced',
            price=Decimal('9.99'),
            status='published',
            stripe_price_id='price_test123',
        )

        self.url = reverse('subscription_success')

    def test_success_requires_login(self):
        """
        Confirm that an anonymous visitor cannot process a successful
        subscription session.
        """
        response = self.client.get(
            self.url,
            {'session_id': 'cs_test_123'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_success_without_session_id_redirects(self):
        """
        Confirm that a missing Stripe Checkout Session identifier is
        rejected without creating a Subscription record.
        """
        self.client.login(
            username='bob',
            password='pass12345',
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Subscription.objects.filter(
                user=self.user,
            ).exists()
        )

    @patch('plans.views.stripe.checkout.Session.retrieve')
    def test_success_unpaid_session_creates_no_subscription(
        self,
        mock_retrieve,
    ):
        """
        Confirm that an unpaid Stripe session cannot create a local
        subscription.

        This protects the application from granting membership access
        before payment has been completed.
        """
        self.client.login(
            username='bob',
            password='pass12345',
        )

        # Simulate a Stripe session that exists but has not been paid.
        mock_retrieve.return_value = Mock(
            payment_status='unpaid'
        )

        response = self.client.get(
            self.url,
            {'session_id': 'cs_test_123'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Subscription.objects.filter(
                user=self.user,
            ).exists()
        )

    @patch('plans.views.stripe.checkout.Session.retrieve')
    def test_success_paid_session_creates_subscription(
        self,
        mock_retrieve,
    ):
        """
        Confirm that a verified paid Stripe session creates an active
        subscription linked to the correct member and plan.
        """
        self.client.login(
            username='bob',
            password='pass12345',
        )

        # Build a mock Stripe Checkout Session containing the attributes
        # read by the success view.
        session = Mock()
        session.payment_status = 'paid'
        session.subscription = 'sub_test_123'

        # Simulate Stripe's expanded line-item structure so that the view
        # can match the purchased Stripe Price to the correct local plan.
        line_item = Mock()
        line_item.price = Mock(id='price_test123')
        session.line_items = Mock(data=[line_item])

        mock_retrieve.return_value = session

        response = self.client.get(
            self.url,
            {'session_id': 'cs_test_123'},
        )

        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            Subscription.objects.filter(
                user=self.user,
                plan=self.plan,
                status='active',
            ).exists()
        )

    @patch('plans.views.stripe.checkout.Session.retrieve')
    def test_success_does_not_create_duplicate_active_subscription(
        self,
        mock_retrieve,
    ):
        """
        Confirm that processing checkout for an already-active member
        updates the existing subscription rather than creating a duplicate.

        Preventing duplicate active records keeps membership state
        unambiguous and makes repeated success requests idempotent.
        """
        self.client.login(
            username='bob',
            password='pass12345',
        )

        # Create the active local subscription that should be reused.
        Subscription.objects.create(
            user=self.user,
            plan=self.plan,
            status='active',
        )

        session = Mock()
        session.payment_status = 'paid'
        session.subscription = 'sub_test_123'

        line_item = Mock()
        line_item.price = Mock(id='price_test123')
        session.line_items = Mock(data=[line_item])

        mock_retrieve.return_value = session

        self.client.get(
            self.url,
            {'session_id': 'cs_test_123'},
        )

        # There should still be only one active subscription for the user
        # after the success view has processed the repeated request.
        count = Subscription.objects.filter(
            user=self.user,
            status='active',
        ).count()

        self.assertEqual(count, 1)


class PlanManagementTest(TestCase):
    """
    Test staff-only plan-management create, read, update and archive
    operations.

    These tests verify both functional behaviour and authorisation,
    ensuring that ordinary members cannot modify commercially sensitive
    plan information.
    """

    def setUp(self):
        """
        Create staff and non-staff accounts together with a reusable plan.
        """

        # The staff account represents an authorised administrator who may
        # access the custom plan-management interface.
        self.staff = User.objects.create_user(
            'staffmember',
            password='testpass123',
            is_staff=True,
        )

        # The regular account is used to confirm that authentication alone
        # does not grant plan-management permission.
        self.member = User.objects.create_user(
            'regularmember',
            password='testpass123',
        )

        self.plan = Plan.objects.create(
            name='Manage Me',
            slug='manage-me',
            tier='beginner',
            price=9.99,
            status='published',
        )

    def test_non_staff_gets_403(self):
        """
        Confirm that anonymous and authenticated non-staff users receive
        HTTP 403 when accessing plan-management URLs.

        Returning 403 makes clear that the resource exists but the user
        does not have permission to perform the requested action.
        """

        # Test every protected plan-management endpoint rather than only
        # the list page.
        urls = [
            reverse('manage_plans'),
            reverse('plan_create'),
            reverse(
                'plan_edit',
                args=['manage-me'],
            ),
            reverse(
                'plan_archive',
                args=['manage-me'],
            ),
        ]

        # Anonymous access must be forbidden.
        for url in urls:
            self.assertEqual(
                self.client.get(url).status_code,
                403,
            )

        self.client.login(
            username='regularmember',
            password='testpass123',
        )

        # An authenticated account without staff status must also be
        # forbidden.
        for url in urls:
            self.assertEqual(
                self.client.get(url).status_code,
                403,
            )

    def test_staff_sees_all_statuses(self):
        """
        Confirm that staff can view plans regardless of publication state.

        Administrators need access to draft and archived entries so that
        they can review, edit or republish them.
        """
        Plan.objects.create(
            name='Hidden Draft',
            slug='hidden-draft',
            tier='beginner',
            price=5,
            status='draft',
        )

        self.client.login(
            username='staffmember',
            password='testpass123',
        )

        response = self.client.get(
            reverse('manage_plans')
        )

        self.assertContains(response, 'Hidden Draft')
        self.assertContains(response, 'Manage Me')

    def test_staff_can_create_plan_with_features(self):
        """
        Confirm that staff can create a plan and convert the multi-line
        features field into related PlanFeature records.
        """
        self.client.login(
            username='staffmember',
            password='testpass123',
        )

        response = self.client.post(
            reverse('plan_create'),
            {
                'name': 'Created Plan',
                'description': 'A new plan.',
                'tier': 'advanced',
                'price': '19.99',
                'billing_interval': 'monthly',
                'status': 'published',
                'features_text': (
                    'First feature\n'
                    'Second feature'
                ),
            },
        )

        self.assertEqual(response.status_code, 302)

        plan = Plan.objects.get(name='Created Plan')

        # Confirm that the view generated the expected URL-safe slug.
        self.assertEqual(
            plan.slug,
            'created-plan',
        )

        # Confirm that each non-empty line in features_text became a
        # separate related PlanFeature record.
        self.assertEqual(
            plan.features.count(),
            2,
        )

    def test_negative_price_rejected(self):
        """
        Confirm that the PlanForm rejects a price below zero and does not
        save the invalid plan to the database.
        """
        self.client.login(
            username='staffmember',
            password='testpass123',
        )

        response = self.client.post(
            reverse('plan_create'),
            {
                'name': 'Bad Price',
                'description': 'x',
                'tier': 'beginner',
                'price': '-5',
                'billing_interval': 'monthly',
                'status': 'draft',
            },
        )

        # Invalid form submissions should redisplay the form rather than
        # redirecting to the management list.
        self.assertEqual(response.status_code, 200)

        # Confirm that the user receives a meaningful validation message.
        self.assertContains(
            response,
            'positive number',
        )

        # Validation must prevent the invalid model instance from reaching
        # the database.
        self.assertFalse(
            Plan.objects.filter(
                name='Bad Price',
            ).exists()
        )

    def test_staff_can_edit_plan(self):
        """
        Confirm that staff can update an existing plan and replace its
        related feature collection.
        """
        self.client.login(
            username='staffmember',
            password='testpass123',
        )

        response = self.client.post(
            reverse(
                'plan_edit',
                args=['manage-me'],
            ),
            {
                'name': 'Manage Me',
                'description': 'Updated description.',
                'tier': 'intermediate',
                'price': '14.99',
                'billing_interval': 'monthly',
                'status': 'published',
                'features_text': 'Updated feature',
            },
        )

        self.assertEqual(response.status_code, 302)

        # Reload the object so the assertions use the values currently held
        # in the database rather than the original in-memory instance.
        self.plan.refresh_from_db()

        self.assertEqual(
            self.plan.tier,
            'intermediate',
        )
        self.assertEqual(
            self.plan.features.count(),
            1,
        )

    def test_archive_is_soft_delete(self):
        """
        Confirm that archiving changes the plan status instead of deleting
        the database record.

        Soft deletion preserves historical references and allows archived
        plans to be reviewed or restored later.
        """
        self.client.login(
            username='staffmember',
            password='testpass123',
        )

        response = self.client.post(
            reverse(
                'plan_archive',
                args=['manage-me'],
            )
        )

        self.assertEqual(response.status_code, 302)

        self.plan.refresh_from_db()

        self.assertEqual(
            self.plan.status,
            'archived',
        )

    def test_archived_plan_hidden_from_public(self):
        """
        Confirm that an archived plan remains in the database but no longer
        appears on the public plans page.
        """
        self.plan.status = 'archived'
        self.plan.save()

        response = self.client.get(
            reverse('plans')
        )

        self.assertNotContains(
            response,
            'Manage Me',
        )
