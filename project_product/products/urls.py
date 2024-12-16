# from django.urls import path
# from . import views

# app_name = 'products'

# urlpatterns = [
#     path('add/', views.add_product, name='add_product'),
#     path('list/', views.product_list, name='product_list'),
#     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
# ]

# project_product/urls.py

# 

# project_product/apps/products/urls.py

from django.urls import path
from . import views  # Pastikan ini mengacu ke views di aplikasi ini

app_name = 'products'

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('list/', views.product_list, name='product_list'),  # Sesuaikan dengan nama view yang ada di produk
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]