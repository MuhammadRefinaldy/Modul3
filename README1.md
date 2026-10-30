# Sistem Manajemen Perpustakaan

Aplikasi desktop manajemen koleksi buku perpustakaan berbasis **Python** dengan pola arsitektur **MVC (Model-View-Controller)**. Antarmuka dibuat menggunakan **customtkinter** dan data disimpan pada basis data **MySQL**.

## Deskripsi Singkat

Aplikasi ini memungkinkan pengguna mengelola data koleksi buku (judul, penulis, tahun terbit). Akses ke aplikasi dilindungi oleh sistem login:

- **Autentikasi**: pengguna harus login dengan username dan password. Password disimpan dalam bentuk hash SHA-256, bukan teks biasa.
- **Otorisasi (RBAC)**: hak akses ditentukan oleh role pengguna.

| Role | Hak Akses |
|---|---|
| `admin` | Melihat, menambah, memperbarui, dan menghapus data buku |
| `anggota` | Hanya melihat daftar koleksi buku (read-only) |

Fitur lain: tombol **Logout** untuk kembali ke halaman login, pengujian otomatis dengan **pytest**, serta CI pipeline dengan **GitHub Actions**.

## Struktur Direktori MVC

```
modul3/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml     # Konfigurasi CI GitHub Actions
├── config/
│   └── database.py             # Koneksi ke MySQL
├── models/
│   ├── buku_model.py           # Model: query data buku
│   └── user_model.py           # Model: hashing, autentikasi, register user
├── views/
│   ├── buku_view.py            # View: antarmuka form dan tabel buku
│   └── login_view.py           # View: antarmuka login
├── controllers/
│   ├── auth_controller.py      # Controller: alur login
│   └── buku_controller.py      # Controller: logika buku dan otorisasi role
├── tests/
│   ├── test_auth.py            # Unit test autentikasi
│   └── test_buku.py            # Unit test data buku
├── main.py                     # Titik masuk aplikasi
├── requirements.txt            # Daftar dependensi
└── README.md
```

## Panduan Instalasi dan Konfigurasi Database MySQL

### 1. Prasyarat

- Python 3.x
- Laragon (atau MySQL Server lain) dengan layanan MySQL aktif
- Git

### 2. Clone repositori dan siapkan environment

```bash
git clone https://github.com/<username>/<nama-repositori>.git
cd <nama-repositori>

python -m venv env
env\Scripts\activate

pip install -r requirements.txt
```

### 3. Buat database dan tabel

Jalankan Laragon, pastikan MySQL menyala, lalu buka terminal:

```bash
mysql -u root -p
```

```sql
CREATE DATABASE IF NOT EXISTS perpustakaan;
USE perpustakaan;

-- Tabel buku
CREATE TABLE IF NOT EXISTS buku (
    id_buku INT PRIMARY KEY AUTO_INCREMENT,
    judul VARCHAR(255) NOT NULL,
    penulis VARCHAR(150) NOT NULL,
    tahun_terbit INT NOT NULL
);

-- Tabel users
CREATE TABLE IF NOT EXISTS users (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'anggota') NOT NULL DEFAULT 'anggota'
);

-- Akun uji coba (password disimpan sebagai hash SHA-256)
INSERT INTO users (username, password, role) VALUES
('petugas', SHA2('admin123', 256), 'admin'),
('mahasiswa', SHA2('user123', 256), 'anggota');
```

### 4. Sesuaikan konfigurasi koneksi

Buka `config/database.py`, lalu pastikan `host`, `user`, `password`, dan `database` sesuai dengan MySQL di komputer Anda. Pengaturan bawaan Laragon biasanya:

| Parameter | Nilai |
|---|---|
| host | `localhost` |
| user | `root` |
| password | *(kosong)* |
| database | `perpustakaan` |

## Cara Menjalankan Aplikasi

### Dari kode sumber

Pastikan MySQL pada Laragon sudah menyala, lalu:

```bash
python main.py
```

Login menggunakan akun uji coba:

| Username | Password | Role |
|---|---|---|
| `petugas` | `admin123` | admin |
| `mahasiswa` | `user123` | anggota |

### Menjalankan pengujian

```bash
pytest -v
```

### Dari file .exe

Unduh `AplikasiPerpustakaan.exe` pada halaman **Releases** repositori ini, pastikan MySQL pada Laragon sedang menyala, lalu klik dua kali file tersebut.

Untuk membuat file .exe sendiri:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" main.py
```

Hasilnya berada di folder `dist/`.

## CI Pipeline

Setiap `push` atau `pull request` ke branch `main` akan menjalankan workflow GitHub Actions yang meliputi: checkout kode, penyiapan Python 3.11, instalasi dependensi, pengecekan kualitas kode dengan **flake8**, dan pengujian otomatis dengan **pytest**.
