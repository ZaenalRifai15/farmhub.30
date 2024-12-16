from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    deskripsi = models.TextField(null=True, blank=True)
    berat = models.IntegerField(default=1)
    kondisi = models.CharField(max_length=50, default='baru panen')


    def __str__(self):
        return self.name