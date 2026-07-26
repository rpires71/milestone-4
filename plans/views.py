from functools import wraps

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from .forms import PlanForm
from .models import Plan, PlanFeature, Subscription


def all_plans(request):
    """Display all published membership plans."""
    plans = Plan.objects.filter(status='published')
    return render(request, 'plans/plans.html', {'plans': plans})


def plan_detail(request, slug):
    """Display an individual plan with its features."""
    plan = get_object_or_404(Plan, slug=slug, status='published')
    similar_plans = Plan.objects.filter(
        status='published'
    ).exclude(pk=plan.pk)[:3]
    context = {'plan': plan, 'similar_plans': similar_plans}
    return render(request, 'plans/plan_detail.html', context)


@login_required
@require_POST
def subscribe(request, slug):
    """Start a Stripe subscription checkout for a plan."""
    plan = get_object_or_404(Plan, slug=slug, status='published')

    if not plan.stripe_price_id:
        messages.error(request, 'This plan is not available for subscription yet.')
        return redirect('plan_detail', slug=plan.slug)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        mode='subscription',
        line_items=[{'price': plan.stripe_price_id, 'quantity': 1}],
        success_url=request.build_absolute_uri(
            reverse('subscription_success')
        ) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(
            reverse('plan_detail', args=[plan.slug])
        ),
        customer_email=request.user.email or None,
    )
    return redirect(checkout_session.url, code=303)


@login_required
def subscription_success(request):
    """Record the subscription after verifying payment with Stripe."""
    session_id = request.GET.get('session_id')
    if not session_id:
        messages.error(request, 'No checkout session was provided.')
        return redirect('plans')

    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        session = stripe.checkout.Session.retrieve(
            session_id, expand=['line_items']
        )
    # pylint: disable=broad-exception-caught
    except Exception:
        messages.error(request, 'We could not verify your subscription.')
        return redirect('plans')

    # Verify payment actually completed - this closes the free-subscription hole.
    if session.payment_status != 'paid':
        messages.error(request, 'Your subscription payment was not completed.')
        return redirect('plans')

    # Resolve the plan from the Stripe price on the verified session, not from a
    # user-supplied URL parameter. Use attribute access (session is a
    # StripeObject, which does not support .get()).
    price_id = None
    if session.line_items and session.line_items.data:
        price_id = session.line_items.data[0].price.id
    plan = get_object_or_404(Plan, stripe_price_id=price_id)

    # Prevent multiple active subscriptions: update the user's existing active
    # subscription to the new plan rather than creating an additional one.
    existing = Subscription.objects.filter(
        user=request.user, status='active'
    ).first()
    if existing:
        existing.plan = plan
        existing.stripe_subscription_id = session.subscription or ''
        existing.save()
    else:
        Subscription.objects.create(
            user=request.user,
            plan=plan,
            status='active',
            stripe_subscription_id=session.subscription or '',
        )

    messages.success(request, f'You are now subscribed to {plan.name}!')
    return render(request, 'plans/subscription_success.html', {'plan': plan})


def staff_required(view_func):
    """Allow staff only; anyone else gets a 403 (direct URL access included)."""
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped


def _unique_slug(name, instance=None):
    """Build a slug from the name, ensuring uniqueness."""
    base = slugify(name) or 'plan'
    slug = base
    n = 2
    qs = Plan.objects.all()
    if instance is not None and instance.pk:
        qs = qs.exclude(pk=instance.pk)
    while qs.filter(slug=slug).exists():
        slug = f'{base}-{n}'
        n += 1
    return slug


def _sync_features(plan, features_text):
    """Replace the plan's feature lines from the textarea (one per line)."""
    plan.features.all().delete()
    lines = [line.strip() for line in (features_text or '').splitlines() if line.strip()]
    for order, text in enumerate(lines):
        PlanFeature.objects.create(plan=plan, text=text, display_order=order)


@staff_required
def manage_plans(request):
    """Staff-only list of ALL plans (published, draft and archived)."""
    plans = Plan.objects.all().order_by('name')
    return render(request, 'plans/manage_plans.html', {'plans': plans})


@staff_required
def plan_create(request):
    """Create a new plan (staff only). Shares its form with plan_edit."""
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.slug = _unique_slug(plan.name)
            plan.save()
            _sync_features(plan, form.cleaned_data.get('features_text'))
            messages.success(request, f'Plan "{plan.name}" created.')
            return redirect('manage_plans')
        messages.error(request, 'Please correct the highlighted fields below.')
    else:
        form = PlanForm()
    context = {'form': form, 'heading': 'Create New Plan'}
    return render(request, 'plans/plan_form.html', context)


@staff_required
def plan_edit(request, slug):
    """Edit an existing plan (staff only). Shares its form with plan_create."""
    plan = get_object_or_404(Plan, slug=slug)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            _sync_features(plan, form.cleaned_data.get('features_text'))
            messages.success(request, f'Plan "{plan.name}" updated.')
            return redirect('manage_plans')
        messages.error(request, 'Please correct the highlighted fields below.')
    else:
        initial_features = '\n'.join(
            plan.features.values_list('text', flat=True)
        )
        form = PlanForm(instance=plan, initial={'features_text': initial_features})
    context = {'form': form, 'heading': f'Edit Plan: {plan.name}', 'plan': plan}
    return render(request, 'plans/plan_form.html', context)


@staff_required
def plan_archive(request, slug):
    """Archive a plan (soft delete, staff only, behind a confirmation).

    Archiving rather than deleting protects existing subscriptions, which
    reference plans with on_delete=PROTECT.
    """
    plan = get_object_or_404(Plan, slug=slug)
    if request.method == 'POST':
        plan.status = 'archived'
        plan.save()
        messages.success(
            request,
            f'Plan "{plan.name}" archived. It is removed from new sign-ups; '
            'existing subscriptions are not affected.'
        )
        return redirect('manage_plans')
    return render(request, 'plans/plan_confirm_archive.html', {'plan': plan})
