# The views.py file contains the request-handling logic for the Plans
# application. It supports public plan browsing, secure Stripe
# subscription checkout and staff-only plan administration. Helper
# functions are also included to enforce permissions, generate unique
# slugs and synchronise related plan features.

from functools import wraps

# Stripe provides the external payment service used to create and verify
# recurring subscription checkout sessions.
import stripe

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.text import slugify
from django.views.decorators.http import require_POST

# Import the custom form used by staff to create and edit membership plans.
from .forms import PlanForm

# Import the models required for plan presentation, feature management and
# local subscription records.
from .models import Plan, PlanFeature, Subscription


def all_plans(request):
    """
    Display all membership plans that are currently published.

    Filtering at database level prevents draft and archived plans from
    appearing on the public-facing page.
    """
    plans = Plan.objects.filter(status='published')

    return render(
        request,
        'plans/plans.html',
        {'plans': plans},
    )


def plan_detail(request, slug):
    """
    Display one published plan together with its features and alternatives.

    The status restriction ensures that unpublished plans cannot be
    accessed by manually entering their slug into the browser.
    """
    plan = get_object_or_404(
        Plan,
        slug=slug,
        status='published',
    )

    # Stripe returns the member to this page with a query-string flag when
    # checkout is cancelled. The message confirms that no payment was made.
    if request.GET.get('cancelled'):
        messages.info(
            request,
            'Your subscription checkout was cancelled. '
            'You have not been charged.',
        )

    # Present up to three alternative published plans while excluding the
    # plan already being viewed.
    similar_plans = Plan.objects.filter(
        status='published'
    ).exclude(
        pk=plan.pk
    )[:3]

    context = {
        'plan': plan,
        'similar_plans': similar_plans,
    }

    return render(
        request,
        'plans/plan_detail.html',
        context,
    )


@login_required
@require_POST
def subscribe(request, slug):
    """
    Create a Stripe Checkout Session for a published membership plan.

    Authentication connects the future subscription to a known FitHub
    account, while requiring POST prevents checkout from being initiated
    through an ordinary link or page refresh.
    """
    plan = get_object_or_404(
        Plan,
        slug=slug,
        status='published',
    )

    # A Stripe Price identifier is required before Stripe can create a
    # recurring checkout session. Missing configuration is handled within
    # the application instead of sending an invalid request to Stripe.
    if not plan.stripe_price_id:
        messages.error(
            request,
            'This plan is not available for subscription yet.',
        )
        return redirect(
            'plan_detail',
            slug=plan.slug,
        )

    # Read the secret key from environment-backed Django settings rather
    # than storing sensitive credentials directly in source code.
    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        # Subscription mode tells Stripe to create a recurring payment
        # agreement rather than processing a one-time purchase.
        mode='subscription',

        # Use the Stripe Price identifier stored against the verified local
        # plan, with one subscription unit requested.
        line_items=[
            {
                'price': plan.stripe_price_id,
                'quantity': 1,
            }
        ],

        # Stripe replaces the placeholder with the actual Checkout Session
        # identifier before returning the member to FitHub.
        success_url=(
            request.build_absolute_uri(
                reverse('subscription_success')
            )
            + '?session_id={CHECKOUT_SESSION_ID}'
        ),

        # Return cancelled checkouts to the plan detail page with a flag
        # that allows an explanatory message to be displayed.
        cancel_url=(
            request.build_absolute_uri(
                reverse(
                    'plan_detail',
                    args=[plan.slug],
                )
            )
            + '?cancelled=1'
        ),

        # Pre-fill the Stripe form when the member has an email address,
        # while allowing Stripe to request it when the field is empty.
        customer_email=request.user.email or None,
    )

    # HTTP 303 instructs the browser to retrieve the external checkout URL
    # using GET after the original POST request.
    return redirect(
        checkout_session.url,
        code=303,
    )


@login_required
def subscription_success(request):
    """
    Verify a completed Stripe Checkout Session and record the subscription.

    The local Subscription is created or updated only after Stripe confirms
    that payment succeeded. This prevents query-string manipulation from
    granting unpaid membership access.
    """
    session_id = request.GET.get('session_id')

    # The session identifier is required to retrieve and independently
    # verify the checkout result with Stripe.
    if not session_id:
        messages.error(
            request,
            'No checkout session was provided.',
        )
        return redirect('plans')

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        # Expanding line_items makes the purchased Stripe Price available
        # within the same API response, avoiding a separate retrieval call.
        session = stripe.checkout.Session.retrieve(
            session_id,
            expand=['line_items'],
        )

    # Stripe may raise several exception types because of invalid session
    # identifiers, network problems or service errors. The user receives a
    # controlled response rather than an unhandled server error.
    # pylint: disable=broad-exception-caught
    except Exception:
        messages.error(
            request,
            'We could not verify your subscription.',
        )
        return redirect('plans')

    # Confirm that Stripe has marked the checkout as paid before granting
    # or updating subscription access.
    if session.payment_status != 'paid':
        messages.error(
            request,
            'Your subscription payment was not completed.',
        )
        return redirect('plans')

    # Resolve the local plan from the Stripe Price contained in the
    # verified Checkout Session. The application therefore does not trust
    # a plan identifier supplied through the success-page URL.
    price_id = None

    if session.line_items and session.line_items.data:
        price_id = session.line_items.data[0].price.id

    plan = get_object_or_404(
        Plan,
        stripe_price_id=price_id,
    )

    # A member should have no more than one active plan. Reusing the
    # existing record avoids conflicting active subscriptions and makes
    # repeated processing of the success page safer.
    existing = Subscription.objects.filter(
        user=request.user,
        status='active',
    ).first()

    if existing:
        existing.plan = plan
        existing.stripe_subscription_id = (
            session.subscription or ''
        )

        # Saving the existing object records a plan change without creating
        # an additional active Subscription row.
        existing.save()

    else:
        Subscription.objects.create(
            user=request.user,
            plan=plan,
            status='active',
            stripe_subscription_id=session.subscription or '',
        )

    messages.success(
        request,
        f'You are now subscribed to {plan.name}!',
    )

    return render(
        request,
        'plans/subscription_success.html',
        {'plan': plan},
    )


def staff_required(view_func):
    """
    Restrict a view to authenticated staff members.

    The custom decorator returns HTTP 403 for both anonymous and ordinary
    authenticated users, protecting direct URL access to commercial plan
    management functions.
    """

    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        """
        Check the current user's authentication and staff status before
        allowing the protected view to execute.
        """
        if (
            not request.user.is_authenticated
            or not request.user.is_staff
        ):
            raise PermissionDenied

        return view_func(
            request,
            *args,
            **kwargs,
        )

    return _wrapped


def _unique_slug(name, instance=None):
    """
    Generate a URL-safe and unique slug from a plan name.

    When editing a plan, its own database record is excluded from the
    duplicate check so that an unchanged name can retain its current slug.
    """
    base = slugify(name) or 'plan'
    slug = base
    number = 2

    queryset = Plan.objects.all()

    # Exclude the current record during editing so that it does not conflict
    # with its own existing slug.
    if instance is not None and instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Add an incrementing suffix until an unused slug is found.
    while queryset.filter(slug=slug).exists():
        slug = f'{base}-{number}'
        number += 1

    return slug


def _sync_features(plan, features_text):
    """
    Replace a plan's related features using one non-empty line per feature.

    Rebuilding the collection keeps the stored PlanFeature records aligned
    with the contents of the staff-facing textarea after either creation
    or editing.
    """

    # Remove the old feature collection before constructing the newly
    # submitted version.
    plan.features.all().delete()

    # Strip surrounding whitespace and ignore empty lines so that accidental
    # blank entries do not produce empty database records.
    lines = [
        line.strip()
        for line in (features_text or '').splitlines()
        if line.strip()
    ]

    # Preserve the submitted order through display_order values.
    for order, text in enumerate(lines):
        PlanFeature.objects.create(
            plan=plan,
            text=text,
            display_order=order,
        )


@staff_required
def manage_plans(request):
    """
    Display every plan to authorised staff members.

    Unlike the public plans page, this management view includes published,
    draft and archived records so that the complete plan lifecycle can be
    administered.
    """
    plans = Plan.objects.all().order_by('name')

    return render(
        request,
        'plans/manage_plans.html',
        {'plans': plans},
    )


@staff_required
def plan_create(request):
    """
    Create a new membership plan through the staff management interface.

    The same PlanForm is shared with the editing workflow to keep
    validation, field presentation and business rules consistent.
    """
    if request.method == 'POST':
        form = PlanForm(request.POST)

        if form.is_valid():
            # Delay the initial database save so that a unique slug can be
            # assigned to the model instance first.
            plan = form.save(commit=False)
            plan.slug = _unique_slug(plan.name)
            plan.save()

            # Convert the multi-line textarea into ordered PlanFeature
            # records associated with the newly created plan.
            _sync_features(
                plan,
                form.cleaned_data.get('features_text'),
            )

            messages.success(
                request,
                f'Plan "{plan.name}" created.',
            )
            return redirect('manage_plans')

        # Redisplay the bound form so that validation errors and the user's
        # original values remain visible.
        messages.error(
            request,
            'Please correct the highlighted fields below.',
        )

    else:
        # An unbound form is used when staff first open the creation page.
        form = PlanForm()

    context = {
        'form': form,
        'heading': 'Create New Plan',
    }

    return render(
        request,
        'plans/plan_form.html',
        context,
    )


@staff_required
def plan_edit(request, slug):
    """
    Update an existing plan through the staff management interface.

    Existing feature records are presented as one line per feature and are
    synchronised after a valid submission.
    """
    plan = get_object_or_404(
        Plan,
        slug=slug,
    )

    if request.method == 'POST':
        # Passing the existing instance changes the ModelForm operation
        # from object creation to object update.
        form = PlanForm(
            request.POST,
            instance=plan,
        )

        if form.is_valid():
            form.save()

            _sync_features(
                plan,
                form.cleaned_data.get('features_text'),
            )

            messages.success(
                request,
                f'Plan "{plan.name}" updated.',
            )
            return redirect('manage_plans')

        messages.error(
            request,
            'Please correct the highlighted fields below.',
        )

    else:
        # Convert related PlanFeature records back into the textarea format
        # expected by the shared form.
        initial_features = '\n'.join(
            plan.features.values_list(
                'text',
                flat=True,
            )
        )

        form = PlanForm(
            instance=plan,
            initial={
                'features_text': initial_features,
            },
        )

    context = {
        'form': form,
        'heading': f'Edit Plan: {plan.name}',
        'plan': plan,
    }

    return render(
        request,
        'plans/plan_form.html',
        context,
    )


@staff_required
def plan_archive(request, slug):
    """
    Archive a membership plan following staff confirmation.

    Archiving is used as a soft-delete strategy because subscriptions refer
    to plans using on_delete=PROTECT. Retaining the Plan record preserves
    historical subscription relationships and commercial records.
    """
    plan = get_object_or_404(
        Plan,
        slug=slug,
    )

    if request.method == 'POST':
        # Changing the status removes the plan from new public sign-ups
        # without deleting the underlying record.
        plan.status = 'archived'
        plan.save()

        messages.success(
            request,
            f'Plan "{plan.name}" archived. '
            'It is removed from new sign-ups; '
            'existing subscriptions are not affected.',
        )

        return redirect('manage_plans')

    # GET presents a confirmation page so that archiving cannot occur
    # accidentally through ordinary navigation.
    return render(
        request,
        'plans/plan_confirm_archive.html',
        {'plan': plan},
    )
