"""Views for the member dashboard and profile editing."""

# accounts/views.py
# flash messages (success/error banners)
from django.contrib import messages
# decorator that gates a view behind login
from django.contrib.auth.decorators import login_required
# render = HTML response; redirect = send elsewhere
from django.shortcuts import redirect, render
# build a URL from its name
from django.urls import reverse

from .forms import FitnessProfileForm
from .models import Profile

# Tab IDs the dashboard is allowed to reopen via ?tab=<value> after a
# redirect. Whitelisted server-side so the query param can't be used to
# inject an arbitrary selector into the page.
DASHBOARD_TABS = {'overview', 'details', 'subscription', 'orders', 'saved-community'}


def profile_is_complete(profile):
    """A profile counts as complete once goal and experience are both set."""
    # A plain helper function (not a view). bool(...) collapses the checks to
    # True/False: True only if profile exists AND both fields are truthy.
    # Extracting this keeps the "what does complete mean?" rule in ONE place,
    # used by both dashboard and profile_setup â€” the DRY principle.
    return bool(profile and profile.fitness_goal and profile.experience_level)


# @login_required is a DECORATOR â€” it wraps the view so that if an anonymous user
# requests it, Django redirects them to the login page instead of running the view.
# This is your access control, declared in one line.
@login_required
def dashboard(request):
    """Member dashboard showing subscription, orders and profile."""
    # Every view receives 'request' â€” an object holding everything about the
    # incoming HTTP request (the logged-in user, GET/POST data, method, etc.).
    user = request.user

    # First-time users (incomplete profile) are sent to step 2 once.
    # getattr(user, 'profile', None) safely fetches user.profile, returning None
    # if it doesn't exist yet (rather than crashing). New users get redirected to
    # the one-time setup step. This is the "gate incomplete profiles" rule.
    profile = getattr(user, 'profile', None)
    if not profile_is_complete(profile):
        return redirect('profile_setup')

    # Active subscription (most recent active one, if any)
    # user.subscriptions works because of the related_name on the Subscription
    # model's ForeignKey. .all() gets them; .order_by('-created_at') sorts newest
    # first (the minus means descending). This is the Django ORM â€” Python that
    # becomes SQL.
    subscriptions = user.subscriptions.all().order_by('-created_at')
    active_subscription = subscriptions.filter(status='active').first()

    # Orders
    # Same pattern for orders. Slicing [:5] becomes SQL LIMIT 5 â€” efficient,
    # it doesn't load all orders then trim in Python.
    orders = user.orders.all().order_by('-created_at')
    recent_orders = orders[:5]

    # Profile (created via OneToOne; may not exist yet)
    profile = getattr(user, 'profile', None)
    # Build the profile form bound to the existing profile, so the dashboard can
    # render it pre-filled. instance=profile ties the form to that DB row.
    profile_form = FitnessProfileForm(instance=profile)

    # request.GET holds query-string params (?tab=details). Only accept the value
    # if it's in our whitelist â€” otherwise active_tab stays None. Security habit again.
    requested_tab = request.GET.get('tab')
    active_tab = requested_tab if requested_tab in DASHBOARD_TABS else None

    # The context dict is the bridge from view to template: every key here becomes
    # a variable available in dashboard.html (e.g. {{ order_count }}).
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
    # render() combines the template with the context and returns an HTTP response.
    return render(request, 'accounts/dashboard.html', context)


@login_required
def profile_setup(request):
    """Collect fitness details in the one-time Step 2 flow after registration."""
    # get_or_create returns (object, created_bool). It fetches the profile if it
    # exists, or creates one if not â€” so this view never crashes on a missing
    # profile. The "_" ignores the created flag (we don't need to know which).
    profile, _ = Profile.objects.get_or_create(user=request.user)

    # If setup is already done, don't show it again â€” UNLESS this is a POST
    # (they're submitting the form), which we must still process.
    if profile_is_complete(profile) and request.method != "POST":
        return redirect("dashboard")

    # THE CORE VIEW PATTERN â€” branch on the HTTP method:
    if request.method == "POST":
        # POST = the user submitted the form. Bind the form to their input
        # (request.POST) AND the existing profile (instance=profile).
        form = FitnessProfileForm(request.POST, instance=profile)
        if form.is_valid():          # run all validation
            form.save()              # write to the DB
            return redirect("dashboard")   # PRG pattern: redirect after a successful POST
        # (if invalid, we fall through and re-render the form WITH its errors)
    else:
        # GET = the user is just viewing the page. Show an unbound-but-prefilled form.
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
    # reverse('dashboard') builds the dashboard URL from its name, then we append
    # the query string to reopen the details tab. Building URLs from names (not
    # hardcoded paths) is why the name= in urls.py mattered.
    dashboard_details_url = f"{reverse('dashboard')}?tab=details"

    # This view ONLY handles form submission. A non-POST request (someone hitting
    # the URL directly) just bounces back to the dashboard â€” the form itself lives
    # on the dashboard, not on a separate page.
    if request.method != "POST":
        return redirect(dashboard_details_url)

    form = FitnessProfileForm(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        # messages.success queues a one-time flash banner shown on the next page.
        messages.success(request, "Profile updated successfully.")
    else:
        # On failure, surface each validation error as a flash message. The nested
        # loop walks form.errors (a dict of field -> list of errors). "_" ignores
        # the field name; we just show each error string.
        for _, errors in form.errors.items():
            for error in errors:
                messages.error(request, error)

    # Either way, redirect back to the dashboard details tab (PRG pattern again).
    return redirect(dashboard_details_url)
