import sys
import csv
from getpass import getpass
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, ChannelParticipantsSearch
from telethon.errors import (
    SessionPasswordNeededError, 
    UsernameNotOccupiedError, 
    FloodWaitError, 
    ChatAdminRequiredError
)
import time

# --- KONFIGURASI ---
# Dapatkan di https://my.telegram.org
API_ID = 0 
API_HASH = ''
PHONE = '' # Gunakan format internasional: +628...

def main():
    print("--- Telegram Member Scraper by SPY-E ---")
    
    client = TelegramClient('session_spye', API_ID, API_HASH)
    
    try:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(PHONE)
            try:
                client.sign_in(PHONE, input('Masukkan Kode Verifikasi: '))
            except SessionPasswordNeededError:
                client.sign_in(password=getpass('Masukkan Password 2FA: '))
        
        print(f"Berhasil Login sebagai: {client.get_me().first_name}")

        # Input target
        target_attr = input("Masukkan Username Grup/Channel (tanpa @): ")
        
        try:
            entity = client.get_entity(target_attr)
        except UsernameNotOccupiedError:
            print("Error: Username tidak ditemukan!")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

        print(f"Mengambil data dari: {entity.title}")
        
        all_participants = []
        offset = 0
        limit = 100
        
        while True:
            try:
                # Menggunakan method modern get_participants
                participants = client.get_participants(entity, limit=limit, offset=offset, aggressive=True)
                if not participants:
                    break
                
                all_participants.extend(participants)
                offset += len(participants)
                
                print(f"Sedang memproses... {len(all_participants)} user terkumpul", end="\r")
                time.sleep(1) # Jeda untuk menghindari FloodWait
                
            except ChatAdminRequiredError:
                print("\nError: Kamu harus menjadi admin/member untuk melihat daftar ini.")
                break
            except FloodWaitError as e:
                print(f"\nTerkena Limit! Tunggu {e.seconds} detik.")
                time.sleep(e.seconds)
            except Exception as e:
                print(f"\nTerjadi kesalahan: {e}")
                break

        # Simpan ke CSV (Lebih rapi dari .txt)
        filename = f"members_{target_attr}.csv"
        with open(filename, "w", encoding='UTF-8', newline='') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['User ID', 'Username', 'First Name', 'Last Name', 'Status'])
            
            for user in all_participants:
                username = user.username if user.username else ""
                first_name = user.first_name if user.first_name else ""
                last_name = user.last_name if user.last_name else ""
                # Deteksi status bot atau user biasa
                status = "Bot" if user.bot else "User"
                
                writer.writerow([user.id, username, first_name, last_name, status])

        print(f"\nSelesai! {len(all_participants)} data disimpan ke {filename}")

    except Exception as e:
        print(f"Gagal koneksi: {e}")
    finally:
        client.disconnect()

if __name__ == '__main__':
    main()
