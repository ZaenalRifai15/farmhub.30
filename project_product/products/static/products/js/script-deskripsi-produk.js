document.addEventListener("DOMContentLoaded", () => {
    // Simulasi nyokot data produk ti URL
    const urlParams = new URLSearchParams(window.location.search);
    const productId = urlParams.get("id");

    // nyokot data produk ti backend
    fetch(`http://127.0.0.1:8000/api/products/${productId}/`)
        .then(response => response.json())
        .then(data => {
            // Update halaman ku detail produk
            document.getElementById("product-image").src = data.image;
            document.getElementById("product-name").textContent = data.name;
            document.getElementById("product-weight").textContent = data.weight;
            document.getElementById("product-price").textContent = data.price;
            document.getElementById("product-description").textContent = data.description;

            // Update informasi penjual
            document.getElementById("seller-name").textContent = data.seller.name;
            document.getElementById("seller-location").textContent = data.seller.location;
        })
        .catch(error => console.error("Error fetching product details:", error));
});

// Fungsi keur kembali
function goBack() {
    window.history.back();
}

//Django na (ceuk gpt)

        // views.py (meren)
// from django.http import JsonResponse

// def get_product_detail(request, product_id):
//     data = {
//         "id": product_id,
//         "name": "Sawi Hijau",
//         "weight": "1 ikat",
//         "price": "Rp9.500",
//         "description": "Sawi hijau segar langsung dari petani lokal.",
//         "image": "url_sawi_image",
//         "seller": {
//             "name": "Pak Budi",
//             "location": "Sukajadi, Bandung"
//         }
//     }
//     return JsonResponse(data)

        //urls.py
// from django.urls import path
// from .views import get_product_detail

// urlpatterns = [
//     path('api/products/<int:product_id>/', get_product_detail),
// ]

