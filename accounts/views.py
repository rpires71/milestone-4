from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
