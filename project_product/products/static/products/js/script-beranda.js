document.addEventListener("DOMContentLoaded", () => {
    // Simulasi API ker nyokot lokasi dan produk
    fetch("http://127.0.0.1:8000/api/products/")
        .then(response => response.json())
        .then(data => {
            // Update lokasi pengguna di header
            document.getElementById("user-location").textContent = data.location;

            // Update 'produk terdekat'
            const terdekatContainer = document.getElementById("terdekat-products");
            data.terdekat.forEach(product => {
                const productCard = createProductCard(product);
                terdekatContainer.appendChild(productCard);
            });

            // Update 'produk paling laku'
            const palingLakuContainer = document.getElementById("paling-laku-products");
            data.paling_laku.forEach(product => {
                const productCard = createProductCard(product);
                palingLakuContainer.appendChild(productCard);
            });
        })
        .catch(error => console.error("Error fetching data:", error));

    // sidebar
    const menuButton = document.getElementById("menu-button");
    const sidebar = document.getElementById("sidebar");

    // sidebar katingali
    menuButton.addEventListener("click", () => {
        sidebar.classList.toggle("active");
    });
});

// Fungsi ker nyien kartu produk
function createProductCard(product) {
    const card = document.createElement("div");
    card.classList.add("product-item");

    card.innerHTML = `
        <img src="${product.image}" alt="${product.name}">
        <h4>${product.name}</h4>
        <p>${product.weight}</p>
        <p><strong>${product.price}</strong></p>
    `;
    return card;
}


// contoh django views.py (ti gpt)

// from django.http import JsonResponse

// def get_products(request):
//     data = {
//         "location": "Sukajadi, Bandung",
//         "terdekat": [
//             {"name": "Sawi Hijau", "weight": "1 ikat", "price": "Rp9.500", "image": "url_sawi_image"},
//             {"name": "Tomat", "weight": "1 kg", "price": "Rp9.500", "image": "url_tomat_image"},
//         ],
//         "paling_laku": [
//             {"name": "Sawi Hijau", "weight": "1 ikat", "price": "Rp9.500", "image": "url_sawi_image"},
//             {"name": "Tomat", "weight": "1 kg", "price": "Rp9.500", "image": "url_tomat_image"},
//         ]
//     }
//     return JsonResponse(data)
