from django.urls import path, include

from rest_framework.authtoken import views

# from the views.py file, which is inside the same directory import home method
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
]
