import os

files = ['dashboard.html', 'orders.html', 'order-detail.html', 'menu-management.html', 'settings.html']

translations = {
    "</i> Delivery": "</i> Pengiriman",
    "</i> Pickup": "</i> Ambil Sendiri",
    "Order Type": "Tipe Pesanan",
    "Delivery Address": "Alamat Pengiriman",
    "Delivery Notes": "Catatan Pengiriman",
    "Customer Details": "Detail Pelanggan",
    "Customer Info": "Info Pelanggan",
    "Payment Method": "Metode Pembayaran",
    "Order Status": "Status Pesanan",
    "Order Placed": "Pesanan Dibuat",
    "Ready for Pickup": "Siap untuk Diambil",
    "On the Way": "Dalam Perjalanan",
    "Delivered": "Terkirim",
    "Preparing": "Menyiapkan",
    "New": "Baru",
    "View All": "Lihat Semua",
    "All Items": "Semua Item",
    "Item Name": "Nama Item",
    "Category": "Kategori",
    "Price": "Harga",
    "Actions": "Aksi",
    "Out of Stock": "Habis",
    "Add New Menu Item": "Tambah Item Menu Baru",
    "Upload Image": "Unggah Gambar",
    "Price (Rp)": "Harga (Rp)",
    "Description": "Deskripsi",
    "Cancel": "Batal",
    "Save Item": "Simpan Item",
    "Store Settings": "Pengaturan Toko",
    "Store Status": "Status Toko",
    "Temporarily close your store from receiving new orders.": "Tutup sementara toko Anda dari menerima pesanan baru.",
    "Currently Open": "Saat Ini Buka",
    "Store Information": "Informasi Toko",
    "Store Name": "Nama Toko",
    "Phone Number": "Nomor Telepon",
    "Operating Hours": "Jam Operasional",
    "Monday - Saturday": "Senin - Sabtu",
    "Sunday": "Minggu",
    "Delivery Settings": "Pengaturan Pengiriman",
    "Max Delivery Radius (km)": "Radius Pengiriman Maksimal (km)",
    "Standard Delivery Fee (Rp)": "Ongkos Kirim Standar (Rp)",
    "Minimum Order Amount (Rp)": "Minimum Pesanan (Rp)",
    "Free Delivery Above (Rp)": "Gratis ongkir di atas (Rp)",
    "Save Changes": "Simpan Perubahan",
    "Action Required": "Perlu Tindakan",
    "In Progress &amp; Completed": "Sedang Berjalan & Selesai",
    "In Progress & Completed": "Sedang Berjalan & Selesai",
    "Mark Ready": "Tandai Siap",
    "Assign Driver": "Tugaskan Kurir",
    "Mark Delivered": "Tandai Terkirim",
    "Mark as Ready": "Tandai Siap",
    "Order Items": "Item Pesanan",
    "Subtotal": "Subtotal",
    "Delivery Fee": "Ongkos Kirim",
    "Paid": "Dibayar",
    "Name": "Nama",
    "Phone": "Telepon",
    "Pending": "Tertunda",
    "Menu Management - Cafe Olga Admin": "Manajemen Menu - Cafe Olga Admin",
    "Add New Item": "Tambah Item Baru",
}

for filename in files:
    filepath = os.path.join('/Users/ericanthony/Projects/online-cafe-olga/admin', filename)
    with open(filepath, 'r') as f:
        content = f.read()
        
    for k, v in translations.items():
        content = content.replace(k, v)
        
    with open(filepath, 'w') as f:
        f.write(content)

print("Done phase 3")
