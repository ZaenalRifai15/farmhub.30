from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):  # Nama model diubah menjadi 'CustomUser'
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    tanggal_lahir = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    deskripsi = models.TextField(null=True, blank=True)
    berat = models.IntegerField(default=1)
    kondisi = models.CharField(max_length=50, default='baru panen')

    def __str__(self):
        return self.name
