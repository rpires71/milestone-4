from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('shop.urls')),
    path('plans/', include('plans.urls')),
    path('reviews/', include('reviews.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('community/', include('community.urls')),
    path('dashboard/', include('accounts.urls')),
    path('', include('home.urls')),
]