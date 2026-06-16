from django.shortcuts import render, get_object_or_404
from .models import Plan


def all_plans(request):
    """Display all published membership plans."""
    plans = Plan.objects.filter(status='published')
    return render(request, 'plans/plans.html', {'plans': plans})


def plan_detail(request, slug):
    """Display an individual plan with its features."""
    plan = get_object_or_404(Plan, slug=slug, status='published')
    return render(request, 'plans/plan_detail.html', {'plan': plan})