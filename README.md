# ☕ Warkop Simulasi Kasir

Aplikasi ini adalah program berbasis **Command Line Interface (CLI)** sederhana yang mensimulasikan sistem pembelian di sebuah warung kopi bernama **Warkop Madura**.  
Pengguna dapat memilih menu, menambahkan pesanan, dan melihat total harga dari pembelian mereka.

---

## 📋 Fitur Utama

- Menampilkan daftar menu yang tersedia.  
- Memungkinkan pengguna memilih barang berdasarkan nomor menu.  
- Menyimpan daftar barang yang dibeli sementara.  
- Menampilkan ringkasan belanja dan total harga di akhir.  
- Menghentikan proses pembelian kapan saja dengan perintah `n`.

---

## 🧠 Konsep yang Digunakan

Program ini menggunakan konsep dasar Python seperti:
- **List dan Dictionary** untuk menyimpan data menu dan transaksi.  
- **Fungsi (`def`)** untuk modularisasi kode (`list_barang()` menampilkan menu).  
- **Loop (`while True`)** untuk membuat interaksi terus berjalan sampai pengguna berhenti.  
- **Try–Except** untuk menangani input yang tidak valid.  
- **Modul `sys`** untuk membersihkan output terminal (efek visual agar rapi).  

---

## 🚀 Cara Menjalankan Program

### 1. Persiapan
Pastikan kamu sudah menginstal **Python 3.x** di perangkatmu.  
Cek versi dengan menjalankan perintah berikut di terminal:

```bash
python --version
