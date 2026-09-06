import os
import re

files = ['dashboard.html', 'orders.html', 'order-detail.html', 'menu-management.html', 'settings.html']

translations = {
    ">Edit<": ">Ubah<",
    ">Delete<": ">Hapus<",
    ">Save<": ">Simpan<",
    ">Search<": ">Cari<",
    ">Filter<": ">Filter<",
    ">In Stock<": ">Tersedia<",
    ">Open<": ">Buka<",
    ">Closed<": ">Tutup<",
    "Welcome back": "Selamat datang kembali",
    "Good morning": "Selamat pagi",
    "Good afternoon": "Selamat siang",
    "Good evening": "Selamat malam",
    ">Back<": ">Kembali<",
    ">Payment<": ">Pembayaran<",
    ">Delivery<": ">Pengiriman<",
    ">Pickup<": ">Ambil Sendiri<",
    "Customer Info": "Info Pelanggan",
    "Order Info": "Info Pesanan",
    "Order Timeline": "Riwayat Status",
    "Order Confirmed": "Pesanan Dikonfirmasi",
    "Delivery Type": "Tipe Pengiriman",
    "Reset Password": "Reset Kata Sandi",
    "Popular Items": "Item Populer",
}

for filename in files:
    filepath = os.path.join('/Users/ericanthony/Projects/online-cafe-olga/admin', filename)
    with open(filepath, 'r') as f:
        content = f.read()
        
    for k, v in translations.items():
        content = content.replace(k, v)
        
    with open(filepath, 'w') as f:
        f.write(content)

print("Done phase 2")
