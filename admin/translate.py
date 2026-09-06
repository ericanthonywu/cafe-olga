import os
import re

files = ['dashboard.html', 'orders.html', 'order-detail.html', 'menu-management.html', 'settings.html']

translations = {
    ">Dashboard<": ">Dasbor<",
    ">Orders<": ">Pesanan<",
    ">Menu Management<": ">Manajemen Menu<",
    ">Settings<": ">Pengaturan<",
    ">View Store<": ">Lihat Toko<",
    ">Logout<": ">Keluar<",
    
    "Dashboard - Cafe Olga Admin": "Dasbor - Cafe Olga Admin",
    "Welcome back, Admin 👋": "Selamat datang kembali, Admin 👋",
    "Here's what's happening at Cafe Olga today.": "Berikut adalah hal yang terjadi di Cafe Olga hari ini.",
    "Today's Orders": "Pesanan Hari Ini",
    "from yesterday": "dari kemarin",
    "Revenue": "Pendapatan",
    "Avg Order Value": "Rata-rata Nilai Pesanan",
    "Stable": "Stabil",
    "Pending Orders": "Pesanan Tertunda",
    "Requires action": "Perlu tindakan",
    "Recent Orders": "Pesanan Terbaru",
    "View All": "Lihat Semua",
    "Popular Items Today": "Item Populer Hari Ini",
    "orders</": "pesanan</",
    "Order ID": "ID Pesanan",
    "Customer": "Pelanggan",
    "Items": "Item",
    "Total": "Total",
    "Status": "Status",
    "Time": "Waktu",
    
    ">Preparing<": ">Menyiapkan<",
    " Preparing": " Menyiapkan",
    ">Ready<": ">Siap<",
    " Ready": " Siap",
    ">On the Way<": ">Dalam Perjalanan<",
    " On the Way": " Dalam Perjalanan",
    ">Delivered<": ">Terkirim<",
    " Delivered": " Terkirim",
    ">New<": ">Baru<",
    ">All (": ">Semua (",
    "Action Required": "Perlu Tindakan",
    
    "Orders - Cafe Olga Admin": "Pesanan - Cafe Olga Admin",
    'placeholder="Search orders..."': 'placeholder="Cari pesanan..."',
    ">Accept<": ">Terima<",
    ">Reject<": ">Tolak<",
    "In Progress &amp; Completed": "Sedang Berjalan & Selesai",
    "In Progress & Completed": "Sedang Berjalan & Selesai",
    ">Mark Ready<": ">Tandai Siap<",
    ">Assign Driver<": ">Tugaskan Kurir<",
    ">Mark Delivered<": ">Tandai Terkirim<",
    
    "Order Detail - Cafe Olga Admin": "Detail Pesanan - Cafe Olga Admin",
    "Order Details": "Detail Pesanan",
    ">Mark as Ready<": ">Tandai Siap<",
    "Order Items": "Item Pesanan",
    "Notes:": "Catatan:",
    ">Subtotal<": ">Subtotal<",
    "Delivery Fee": "Ongkos Kirim",
    ">Payment Method<": ">Metode Pembayaran<",
    ">Paid<": ">Dibayar<",
    "Customer Details": "Detail Pelanggan",
    ">Name<": ">Nama<",
    ">Phone<": ">Telepon<",
    "Order Type": "Tipe Pesanan",
    "Delivery Address": "Alamat Pengiriman",
    "Delivery Notes": "Catatan Pengiriman",
    "Order Status": "Status Pesanan",
    "Order Placed": "Pesanan Dibuat",
    "Ready for Pickup": "Siap untuk Diambil",
    ">Pending<": ">Tertunda<",
    
    "Menu Management - Cafe Olga Admin": "Manajemen Menu - Cafe Olga Admin",
    "Add New Item": "Tambah Item Baru",
    "All Items": "Semua Item",
    "Item Name": "Nama Item",
    ">Category<": ">Kategori<",
    ">Price<": ">Harga<",
    "Actions": "Aksi",
    "Out of Stock": "Habis",
    "Add New Menu Item": "Tambah Item Menu Baru",
    "Upload Image": "Unggah Gambar",
    "Price (Rp)": "Harga (Rp)",
    ">Description<": ">Deskripsi<",
    ">Cancel<": ">Batal<",
    "Save Item": "Simpan Item",
    
    "Settings - Cafe Olga Admin": "Pengaturan - Cafe Olga Admin",
    "Store Settings": "Pengaturan Toko",
    "Store Status": "Status Toko",
    "Temporarily close your store from receiving new orders.": "Tutup sementara toko Anda dari menerima pesanan baru.",
    "Currently Open": "Saat Ini Buka",
    "Store Information": "Informasi Toko",
    "Store Name": "Nama Toko",
    "Phone Number": "Nomor Telepon",
    ">Address<": ">Alamat<",
    "Operating Hours": "Jam Operasional",
    "Monday - Saturday": "Senin - Sabtu",
    ">Sunday<": ">Minggu<",
    "Delivery Settings": "Pengaturan Pengiriman",
    "Max Delivery Radius (km)": "Radius Pengiriman Maksimal (km)",
    "Standard Delivery Fee (Rp)": "Ongkos Kirim Standar (Rp)",
    "Minimum Order Amount (Rp)": "Minimum Pesanan (Rp)",
    "Free Delivery Above (Rp)": "Gratis ongkir di atas (Rp)",
    "Save Changes": "Simpan Perubahan",
    
    # Specific attributes
    'placeholder="e.g. Vanilla Latte"': 'placeholder="mis. Vanilla Latte"',
    'placeholder="Brief description of the item..."': 'placeholder="Deskripsi singkat item..."',
    'value="Cafe Olga"': 'value="Cafe Olga"', # no change
}

for filename in files:
    filepath = os.path.join('/Users/ericanthony/Projects/online-cafe-olga/admin', filename)
    with open(filepath, 'r') as f:
        content = f.read()
        
    for k, v in translations.items():
        content = content.replace(k, v)
        
    # Replace cases like "Placed on 5 Sep 2026 at 10:33 AM" 
    # Just basic regex for english date string if needed, but not strictly requested.
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Done")
