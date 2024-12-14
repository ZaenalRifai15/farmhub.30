from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('', views.product_list, name='product_list'),
    path('detail/', views.detail, name='detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
