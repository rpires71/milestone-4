from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_plans, name='plans'),
    path('manage/', views.manage_plans, name='manage_plans'),
    path('manage/new/', views.plan_create, name='plan_create'),
    path('manage/<slug:slug>/edit/', views.plan_edit, name='plan_edit'),
    path('manage/<slug:slug>/archive/', views.plan_archive, name='plan_archive'),
    path('subscribe/<slug:slug>/', views.subscribe, name='subscribe'),
    path('subscription/success/', views.subscription_success, name='subscription_success'),
    path('<slug:slug>/', views.plan_detail, name='plan_detail'),
]
