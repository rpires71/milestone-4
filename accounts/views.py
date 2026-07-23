"""Views for the member dashboard and profile editing."""

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import FitnessProfileForm
from .models import Profile

# Tab IDs the dashboard is allowed to reopen via ?tab=<value> after a
# redirect. Whitelisted server-side so the query param can't be used to
# inject an arbitrary selector into the page.
DASHBOARD_TABS = {'overview', 'details', 'subscription', 'orders', 'saved-community'}


def profile_is_complete(profile):
    """A profile counts as complete once goal and experience are both set."""
    return bool(profile and profile.fitness_goal and profile.experience_level)


@login_required
def dashboard(request):
    """Member dashboard showing subscription, orders and profile."""
    user = request.user

    # First-time users (incomplete profile) are sent to step 2 once.
    profile = getattr(user, 'profile', None)
    if not profile_is_complete(profile):
        return redirect('profile_setup')

    # Active subscription (most recent active one, if any)
    subscriptions = user.subscriptions.all().order_by('-created_at')
    active_subscription = subscriptions.filter(status='active').first()

    # Orders
    orders = user.orders.all().order_by('-created_at')
    recent_orders = orders[:5]

    # Profile (created via OneToOne; may not exist yet)
    profile = getattr(user, 'profile', None)
    profile_form = FitnessProfileForm(instance=profile)

    requested_tab = request.GET.get('tab')
    active_tab = requested_tab if requested_tab in DASHBOARD_TABS else None

    context = {
        'active_subscription': active_subscription,
        'subscription_count': subscriptions.count(),
        'orders': orders,
        'recent_orders': recent_orders,
        'order_count': orders.count(),
        'profile': profile,
        'profile_form': profile_form,
        'active_tab': active_tab,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def profile_setup(request):
    """Collect fitness details in the one-time Step 2 flow after registration."""
    profile, _ = Profile.objects.get_or_create(user=request.user)

    # If they've already completed step 2, don't show it again.
    if profile_is_complete(profile) and request.method != "POST":
        return redirect("dashboard")

    if request.method == "POST":
        form = FitnessProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = FitnessProfileForm(instance=profile)

    return render(request, "accounts/profile_setup.html", {"form": form})


@login_required
def profile_edit(request):
    """Update an existing member's fitness profile from the dashboard.

    Unlike profile_setup (the one-time Step 2 flow after registration),
    this is reachable at any time from the Account Details tab and always
    redirects back to the dashboard rather than gating access to it.
    """
    profile, _ = Profile.objects.get_or_create(user=request.user)
    dashboard_details_url = f"{reverse('dashboard')}?tab=details"

    if request.method != "POST":
        return redirect(dashboard_details_url)

    form = FitnessProfileForm(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, "Profile updated successfully.")
    else:
        for _, errors in form.errors.items():
            for error in errors:
                messages.error(request, error)

    return redirect(dashboard_details_url)
