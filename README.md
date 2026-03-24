# 🛡️ Telegram Member Scraper

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Termux%20|%20Windows%20|%20Linux-orange.svg)

Alat sederhana namun kuat untuk mengumpulkan (scraping) data anggota dari grup atau channel Telegram publik menggunakan Telethon Library. Data yang dikumpulkan disimpan secara otomatis ke dalam format `.csv` yang rapi.

## ✨ Fitur Utama
- **Multi-Platform**: Jalan lancar di Android (Termux), Windows (CMD/PowerShell), dan Linux.
- **Auto-CSV**: Menyimpan ID, Username, Nama Depan, Nama Belakang, dan Status (User/Bot).
- **Anti-Flood**: Dilengkapi jeda waktu (delay) untuk meminimalisir risiko banned/limit.
- **Modern Login**: Mendukung Two-Factor Authentication (2FA).
- **Lightweight**: Ringan dan tidak memerlukan resource besar.

## 🛠️ Persyaratan Sistem
Sebelum menjalankan, pastikan kamu sudah memiliki:
1. **Python 3.8+** terinstall.
2. **API_ID** dan **API_HASH** dari [my.telegram.org](https://my.telegram.org).

## 🚀 Panduan Instalasi

### 📱 Di Termux (Android)
```bash
pkg update && pkg upgrade
pkg install python git
git clone [https://github.com/123tool/Telegram-Member-Scraper.git)
cd Telegram-Member-Scraper
pip install -r requirements.txt
python main.py

```
### 🐧 Di Linux
```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone [https://github.com/USERNAME_KAMU/NAMA_REPO_KAMU.git](https://github.com/USERNAME_KAMU/NAMA_REPO_KAMU.git)
cd NAMA_REPO_KAMU
pip3 install -r requirements.txt
python3 main.py

```
### 📖 Cara Penggunaan
1. ​Buka file main.py menggunakan teks editor (seperti Notepad, VS Code, atau Nano).
2. ​Masukkan API_ID, API_HASH, dan PHONE (Nomor HP akun Telegram kamu) pada bagian konfigurasi.
3. ​Jalankan skrip dengan perintah python main.py.
4. ​Masukkan kode OTP yang dikirim ke Telegram kamu.
5. ​Masukkan username grup target (contoh: grup_diskusi_it) tanpa tanda @.
6. ​Tunggu hingga proses selesai, file .csv akan muncul di folder yang sama.

### ​⚠️ Catatan Penting
​Gunakan alat ini dengan bijak. Penyalahgunaan untuk spamming bukan tanggung jawab pengembang.
​Beberapa grup menyembunyikan daftar anggotanya (Hidden Members). Jika fitur tersebut aktif, skrip ini tidak akan bisa mengambil data secara penuh kecuali kamu adalah Admin.

***​Developed by : SPY-E Building automated solutions for better productivity.***
