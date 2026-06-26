from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import stripe
from .models import Plan, Subscription

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
        ) + f'?plan={plan.slug}',
        cancel_url=request.build_absolute_uri(
            reverse('plan_detail', args=[plan.slug])
        ),
        customer_email=request.user.email or None,
    )
    return redirect(checkout_session.url, code=303)


@login_required
def subscription_success(request):
    """Record the subscription and show a confirmation."""
    slug = request.GET.get('plan')
    plan = get_object_or_404(Plan, slug=slug)

    # Record the subscription (idempotent-ish: avoid duplicates)
    Subscription.objects.get_or_create(
        user=request.user,
        plan=plan,
        defaults={'status': 'active'},
    )
    messages.success(request, f'You are now subscribed to {plan.name}!')
    return render(request, 'plans/subscription_success.html', {'plan': plan})