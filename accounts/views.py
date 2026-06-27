# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FitnessProfileForm
from .models import Profile


@login_required
def dashboard(request):
    """Member dashboard showing subscription, orders and profile."""
    user = request.user

    # Active subscription (most recent active one, if any)
    subscriptions = user.subscriptions.all().order_by('-created_at')
    active_subscription = subscriptions.filter(status='active').first()

    # Orders
    orders = user.orders.all().order_by('-created_at')
    recent_orders = orders[:5]

    # Profile (created via OneToOne; may not exist yet)
    profile = getattr(user, 'profile', None)

    context = {
        'active_subscription': active_subscription,
        'subscription_count': subscriptions.count(),
        'orders': orders,
        'recent_orders': recent_orders,
        'order_count': orders.count(),
        'profile': profile,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def profile_setup(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = FitnessProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = FitnessProfileForm(instance=profile)

    return render(request, "accounts/profile_setup.html", {"form": form})