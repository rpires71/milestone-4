from django.contrib import admin

from .models import Plan, PlanFeature, Subscription


class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 3


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'price', 'billing_interval', 'status')
    list_filter = ('tier', 'billing_interval', 'status')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PlanFeatureInline]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'current_period_end')
    list_filter = ('status',)
