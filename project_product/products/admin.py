from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'berat', 'kondisi')
    search_fields = ('name', 'kondisi') 
    list_filter = ('kondisi',)
    ordering = ('name',) 

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'alamat', 'tanggal_lahir')
    search_fields = ('username',)
    ordering = ('username',)