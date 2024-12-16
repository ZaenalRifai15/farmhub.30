from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
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
    KONDISI_CHOICES = [
        ('baru panen', 'Baru Panen'),
        ('segar', 'Segar'),
        ('kering', 'Kering'),
    ]
    kondisi = models.CharField(max_length=50, choices=KONDISI_CHOICES, default='baru panen')

    KATEGORI_CHOICES = [
        ('Sayuran', 'sayuran'),
        ('Buah', 'buah'),
        ('Hasil Ternak', 'hasil ternak'),
    ]

    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES, default = 'Hasil tani')

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction {self.id} by {self.user.username}'
    


class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    rating = models.PositiveSmallIntegerField()
    komentar = models.TextField()
    id_transaksi = models.OneToOneField(Transaction, on_delete=models.CASCADE, related_name='review')

    def __str__(self):
        return f"Review {self.id_review} for Transaction {self.id_transaksi.id}"
    

class TransactionHistory(models.Model):
    id_history = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction_histories')
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='history_details')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Completed')

    def __str__(self):
        return f"History {self.id_history} for Transaction {self.transaction.id} by {self.user.username}"
    
