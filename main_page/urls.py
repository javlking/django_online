from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('product/<int:pk>/', views.product_info, name='product_about')
]