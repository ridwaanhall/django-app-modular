
# Flowchart

1. Module Management Flow:

   Start
   |
   v
   [Akses halaman module management]
   |
   v
   [Tampilkan daftar module yang tersedia]
   |
   v
   [Pilih aksi]
   |
   +---------------+---------------+
   |               |               |
   v               v               v
   [Install]       [Upgrade]       [Uninstall]
   |               |               |
   v               v               v
   [Jalankan       [Jalankan       [Jalankan
    installer]      upgrader]       uninstaller]
   |               |               |
   v               v               v
   [Update         [Update         [Update
    registry]       registry]       registry]
   |               |               |
   +---------------+---------------+
   |
   v
   [Refresh halaman module management]
   |
   v
   End

2. Role-based Access Flow:

   Start
   |
   v
   [User mengakses halaman produk]
   |
   v
   [Cek role dari user]
   |
   +---------------+---------------+
   |               |               |
   v               v               v
   [Manager]       [User]          [Public]
   |               |               |
   v               v               v
   [Akses CRUD]    [Akses CRU]     [Akses R]
   |               |               |
   +---------------+---------------+
   |
   v
   End

3. Delete Confirmation Flow:

   Start
   |
   v
   [User memilih delete produk]
   |
   v
   [Tampilkan popup konfirmasi]
   |
   v
   [User memilih]
   |
   +---------------+
   |               |
   v               v
   [Ya]            [Tidak]
   |               |
   v               v
   [Delete data]   [Cancel operasi]
   |               |
   +---------------+
   |
   v
   [Refresh halaman daftar produk]
   |
   v
   End
