

from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('list/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('transaction/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('review/<int:transaction_id>/', views.add_review, name='add_review'),
    path('transaction/history/', views.transaction_history, name='riwayat_transaksi'),
]