from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, get_user_model, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import post_save


User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('products:login')
    else:
        form = RegisterForm()
    return render(request, 'products/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Menghapus sesi pengguna sebelumnya (opsional)
            logout(request)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('products:product_list')  # Gunakan nama URL dengan prefiks aplikasi 'products'
            else:
                messages.error(request, "Username atau password salah.")
        else:
            messages.error(request, "Form tidak valid.")
    else:
        form = LoginForm()
    
    return render(request, 'products/login.html', {'form': form})
    
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/deskripsi-produk.html', {'product': product})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/deskripsi-produk.html', {'product': product})

@login_required
def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity

            # Buat transaksi baru
            transaction = Transaction.objects.create(
                user=request.user,
                product=product,
                quantity=quantity,
                total_price=total_price,
            )

            return redirect('products:add_review', transaction_id=transaction.id)
    else:
        form = CheckoutForm()

    # Kirim data produk dan pengguna ke template
    return render(request, 'products/checkout.html', {
        'product': product,
        'user': request.user,
        'form': form,
    })

@login_required


@login_required
def add_review(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)

    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        komentar = request.POST.get('komentar')

        Review.objects.create(
            id_transaksi=transaction,
            rating=rating,
            komentar=komentar
        )
        return redirect('products:transaction_detail', transaction_id=transaction_id)

    return render(request, 'products/add_review.html', {'transaction': transaction})


def transaction_detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)

    review = getattr(transaction, 'review', None)

    return render(request, 'products/transaction_detail.html', {
        'transaction': transaction,
        'review': review
    })


@receiver(post_save, sender=Transaction)
def create_transaction_history(sender, instance, created, **kwargs):
    if created:
        TransactionHistory.objects.create(user=instance.user, transaction=instance, status='Completed')
    else:

        TransactionHistory.objects.create(user=instance.user, transaction=instance, status='Updated')

def transaction_history(request):
    histories = TransactionHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'products/riwayat_transaksi.html', {'histories': histories})