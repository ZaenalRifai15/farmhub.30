from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'berat', 'kondisi')
    search_fields = ('name', 'kondisi') 
    list_filter = ('kondisi',)
    ordering = ('name',) 
