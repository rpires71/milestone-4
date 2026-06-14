from django.contrib import admin
from .models import Plan, PlanFeature, Subscription

admin.site.register(Plan)
admin.site.register(PlanFeature)
admin.site.register(Subscription)