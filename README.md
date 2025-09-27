# Django App Modular

## Project Structure

```txt
django_modular_project/
├── manage.py
├── django_modular_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── module_engine/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── module_engine/
│   │       ├── module_list.html
│   │       └── module_detail.html
|   ├── templatetags/
│   │   ├── __init__.html
│   │   └── module_tags.html
│   ├── urls.py
│   └── views.py
└── product_module/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── templates/
    │   └── product_module/
    │       ├── product_list.html
    │       ├── product_create.html
    │       ├── product_update.html
    │       └── product_detail.html
    ├── urls.py
    └── views.py
```

## Role User

| Username | Role    | Password  |
|----------|---------|-----------|
| admin    | Manager | - |
| user     | User    | - |

## how to use

1. login by access [this url](http://127.0.0.1:8000/login/)
2. enter username and password [reference](#role-user)
3. check [module](http://127.0.0.1:8000/) is installed or not
4. check [product](http://127.0.0.1:8000/product/) to check as public/user/admin

## Flowchart

1. Module Management Flow:

   ```mermaid
   graph TD;
      Start-->A[Akses halaman module management];
      A-->B[Tampilkan daftar module yang tersedia];
      B-->C{Pilih aksi};
      C-->D[Install];
      C-->E[Upgrade];
      C-->F[Uninstall];
      D-->G[Jalankan installer];
      E-->H[Jalankan upgrader];
      F-->I[Jalankan uninstaller];
      G-->J[Update registry];
      H-->J[Update registry];
      I-->J[Update registry];
      J-->K[Refresh halaman module management];
      K-->End;
   ```

2. Role-based Access Flow:

   ```mermaid
   graph TD;
      Start-->A[User mengakses halaman produk];
      A-->B[Cek role dari user];
      B-->C[Manager];
      B-->D[User];
      B-->E[Public];
      C-->F[Akses CRUD];
      D-->G[Akses CRU];
      E-->H[Akses R];
      F-->End;
      G-->End;
      H-->End;
   ```

3. Delete Confirmation Flow:

   ```mermaid
   graph TD;
      Start-->A[User memilih delete produk];
      A-->B[Tampilkan popup konfirmasi];
      B-->C{User memilih};
      C-->D[Ya];
      C-->E[Tidak];
      D-->F[Delete data];
      E-->G[Cancel operasi];
      F-->H[Refresh halaman daftar produk];
      G-->H[Refresh halaman daftar produk];
      H-->End;
   ```

## Django Modular System - Panduan Penggunaan

### Deskripsi Proyek

Project ini adalah sistem Django yang memungkinkan modul diinstal, diupgrade, dan dilepas secara dinamis. Terdiri dari dua komponen utama:

1. **Module Engine** (module_engine) - Sistem untuk manajemen modul
2. **Product Module** (product_module) - Contoh modul yang dapat diinstal/uninstal

### Struktur Modul

- **Module Engine** mengelola siklus hidup modul dengan tindakan install, upgrade, dan uninstall
- **Product Module** menyediakan fitur manajemen produk dengan kontrol akses berbasis role

### Fungsionalitas Utama

#### Module Engine

- Menyediakan halaman untuk mengelola modul (install, upgrade, uninstall)
- Menyimpan status modul di database
- Mengatur akses ke fitur modul berdasarkan status instalasi

#### Product Module

- Menyediakan modul contoh dengan fitur CRUD untuk produk
- Mengimplementasikan 3 role dengan kontrol akses:
  - **Manager**: Akses penuh (CRUD)
  - **User**: Create, Read, Update
  - **Public**: Read only
- Menyediakan konfirmasi dengan popup sebelum menghapus data

### Cara Penggunaan

#### Setup Awal

1. Clone repository atau ekstrak file zip
2. Buat dan aktifkan virtual environment:

   ```bash
   python -m venv venv # atau virtualenv venv
   source venv/bin/activate  ## Di Windows: venv\Scripts\activate
   ```

3. Install dependensi:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan migrasi:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Buat superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Jalankan server:

   ```bash
   python manage.py runserver
   ```

#### Menggunakan Modul Engine

1. Akses `http://127.0.0.1:8000/module/` untuk melihat daftar modul
2. Klik tombol "Install" untuk menginstal modul Product
3. Setelah diinstal, modul akan muncul sebagai "Active"
4. Jika ada perubahan pada struktur database, klik "Upgrade" untuk menerapkan perubahan
5. Untuk menonaktifkan modul, klik "Uninstall"

#### Menggunakan Product Module

1. Setelah module "product_module" diinstal, akses `http://127.0.0.1:8000/product/`
2. Pengguna dengan role berbeda akan melihat UI yang berbeda:
   - Manager dapat melakukan semua operasi (Create, Read, Update, Delete)
   - User dapat membuat, melihat, dan memperbarui produk
   - Public hanya dapat melihat produk

#### Mengatur Role Pengguna

1. Login ke admin panel di `http://127.0.0.1:8000/login/`
2. Buat pengguna baru atau gunakan yang sudah ada
3. Buat entri di model UserRole untuk menghubungkan pengguna dengan role yang diinginkan

### Pengembangan Modul Baru

Untuk membuat modul baru, ikuti pola dari product_module:

1. Buat aplikasi Django baru dengan `python manage.py startapp nama_modul`
2. Buat model yang diperlukan di `models.py`
3. Implementasikan file `installer.py` dengan fungsi `install()`, `upgrade()`, dan `uninstall()`
4. Tambahkan decorator `@module_installed_required` ke semua view
5. Daftarkan modul di Module Engine dengan menambahkan entri di `signals.py`

### Menangani Perubahan Struktur Database

Untuk menangani perubahan struktur database (misalnya menambah field baru):

1. Tambahkan field baru di model
2. Buat migrasi dengan `python manage.py makemigrations nama_modul`
3. Gunakan fitur "Upgrade" di halaman module untuk menerapkan migrasi

### Perhatian Penting

- Uninstall modul tidak menghapus tabel di database, hanya menonaktifkan akses ke modul
- Pastikan bahwa semua modul mendaftar di Module Engine melalui signals
- Gunakan decorator `@module_installed_required` untuk memastikan akses hanya ketika modul diinstal
