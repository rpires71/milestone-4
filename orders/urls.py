from django.urls import path
from . import views
from . import webhooks

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('wh/', webhooks.stripe_webhook, name='stripe_webhook'),
    path('history/', views.order_history, name='order_history'),
    path('history/<order_number>/', views.order_detail, name='order_detail'),
]
