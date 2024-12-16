// // Ambil elemen tombol dan quantity
// const minusBtn = document.querySelector('.qty-btn.minus');
// const plusBtn = document.querySelector('.qty-btn.plus');
// const quantityElement = document.getElementById('quantity');

// // Variabel awal jumlah produk
// let quantity = 2; // Sesuai nilai awal di HTML

// // Fungsi untuk memperbarui tampilan quantity
// function updateQuantity() {
//     quantityElement.textContent = quantity;
// }

// // Event Listener untuk tombol minus
// minusBtn.addEventListener('click', () => {
//     if (quantity > 1) { // Pastikan quantity tidak kurang dari 1
//         quantity--;
//         updateQuantity();
//     }
// });

// // Event Listener untuk tombol plus
// plusBtn.addEventListener('click', () => {
//     quantity++;
//     updateQuantity();
// });

// const unitPrice = 15000; // Harga satuan produk
// const totalPriceElement = document.querySelector('.total-price');

// function updateTotalPrice() {
//     const total = unitPrice * quantity;
//     totalPriceElement.textContent = `Rp${total.toLocaleString('id-ID')}`;
// }

// plusBtn.addEventListener('click', () => {
//     quantity++;
//     updateQuantity();
//     updateTotalPrice();
// });

// minusBtn.addEventListener('click', () => {
//     if (quantity > 1) {
//         quantity--;
//         updateQuantity();
//         updateTotalPrice();
//     }
// });

// Ambil elemen tombol dan elemen lainnya
document.addEventListener("DOMContentLoaded", () => {
    const minusBtn = document.querySelector(".minus");
    const plusBtn = document.querySelector(".plus");
    const quantityDisplay = document.querySelector("#quantity");

    let quantity = parseInt(quantityDisplay.innerText);

    minusBtn.addEventListener("click", () => {
        if (quantity > 1) {
            quantity--;
            quantityDisplay.innerText = quantity;
        }
    });

    plusBtn.addEventListener("click", () => {
        quantity++;
        quantityDisplay.innerText = quantity;
    });
});


// Event listener untuk tombol plus
plusBtn.addEventListener('click', () => {
    quantity++;
    updatePrice();
});

// Inisialisasi tampilan harga saat halaman pertama kali dimuat
updatePrice();