# 🛡️ Telegram Member Scraper - By SPY-E

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
git clone [https://github.com/USERNAME_KAMU/NAMA_REPO_KAMU.git](https://github.com/USERNAME_KAMU/NAMA_REPO_KAMU.git)
cd NAMA_REPO_KAMU
pip install -r requirements.txt
python main.py
