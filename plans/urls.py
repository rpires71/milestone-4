from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_plans, name='plans'),
    path('subscribe/<slug:slug>/', views.subscribe, name='subscribe'),
    path('subscription/success/', views.subscription_success, name='subscription_success'),
    path('<slug:slug>/', views.plan_detail, name='plan_detail'),
]