import os
import time
from datetime import datetime

# ANSI Escape Codes untuk warna
RED = "\033[1;31m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

# Fungsi membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Database barang tersedia
available_items = [
    {'nama': 'Oli Mesin', 'harga': 50000},
    {'nama': 'Busi Motor', 'harga': 15000},
    {'nama': 'Kampas Rem', 'harga': 75000},
    {'nama': 'Aki Motor', 'harga': 300000},
    {'nama': 'Ban Luar', 'harga': 150000},
    {'nama': 'Lampu LED', 'harga': 25000}
]

# Database keranjang belanja
cart_items = []

# Fungsi untuk menampilkan animasi selamat datang
def welcome_animation():
    text = "SELAMAT DATANG DI SAINTEK MOTOR"
    print(CYAN + "\nLoading...\n" + RESET)
    for i in range(len(text) + 1):
        print("\r" + GREEN + text[:i] + RESET, end='', flush=True)
        time.sleep(0.1)
    time.sleep(1)  # Penundaan sebelum melanjutkan ke menu

# Fungsi untuk animasi teks saat memilih menu
def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

# Menampilkan menu utama dengan animasi
def show_menu():
    clear_screen()
    print("\n" + "=" * 40)
    animate_text("SELAMAT DATANG DI SAINTEK MOTOR")
    print("=" * 40)
    animate_text("1. Tambah Barang")
    animate_text("2. Lihat Daftar Barang di Keranjang")
    animate_text("3. Ubah Barang")
    animate_text("4. Hapus Barang")
    animate_text("5. Cetak Struk")
    animate_text("6. Keluar")
    print("=" * 40)
    choice = input("Pilih menu (1-6): ").strip()
    return choice

# Fungsi menampilkan barang yang tersedia dengan animasi
def show_available_items():
    print("\n--- Daftar Barang Tersedia ---")
    print("=" * 40)
    print(f"| {'No':<3} | {'Nama Barang':<15} | {'Harga':<10} |")
    print("=" * 40)
    for i, item in enumerate(available_items, start=1):
        print(f"| {i:<3} | {item['nama']:<15} | {item['harga']:<10} |")
    print("=" * 40)

# Fungsi untuk menambahkan barang ke keranjang dengan animasi
def add_item():
    show_available_items()
    try:
        choice = int(input("Pilih nomor barang (1-6): ").strip()) - 1
        if 0 <= choice < len(available_items):
            selected_item = available_items[choice]
            quantity = int(input(f"Masukkan jumlah '{selected_item['nama']}': ").strip())
            if quantity > 0:
                total = quantity * selected_item['harga']
                cart_items.append({
                    'nama': selected_item['nama'],
                    'jumlah': quantity,
                    'harga': selected_item['harga'],
                    'total': total
                })
                print(f"{GREEN}Barang '{selected_item['nama']}' berhasil ditambahkan ke keranjang!{RESET}\n")
                time.sleep(1)  # Penundaan agar user bisa melihat efek
            else:
                print("Jumlah harus lebih dari 0!\n")
        else:
            print("Nomor barang tidak valid!\n")
    except ValueError:
        print("Input salah! Masukkan angka yang valid.\n")
        time.sleep(1)

# Menampilkan barang dalam keranjang dengan animasi
def show_cart():
    print("\n--- Daftar Barang di Keranjang ---")
    if not cart_items:
        print("Keranjang masih kosong.\n")
        return
    print("=" * 60)
    print(f"| {'No':<3} | {'Nama Barang':<15} | {'Jumlah':<7} | {'Harga':<10} | {'Total':<10} |")
    print("=" * 60)
    for i, item in enumerate(cart_items, start=1):
        print(f"| {i:<3} | {item['nama']:<15} | {item['jumlah']:<7} | {item['harga']:<10.2f} | {item['total']:<10.2f} |")
    print("=" * 60)
    

# Fungsi mencetak struk dengan animasi dan warna
# Fungsi mencetak struk dengan animasi dan warna
def print_receipt():
    if not cart_items:
        print("\nKeranjang belanja kosong!\n")
        return
    total_payment = 0
    
    # Animasi background
    for _ in range(3):  # Loop untuk latar belakang animasi
        clear_screen()  # Membersihkan layar untuk setiap langkah animasi latar belakang
        print(CYAN + "=" * 60 + RESET)
        print(f"{MAGENTA}             STRUK BELANJA SAINTEK MOTOR            {RESET}")
        print(f"{CYAN}            {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
        print("=" * 60)
        print(f"{YELLOW}| {'No':<3} | {'Nama Barang':<15} | {'Jumlah':<7} | {'Harga':<10} | {'Total':<10} |{RESET}")
        print("=" * 60)
        for i, item in enumerate(cart_items, start=1):
            print(f"{GREEN}| {i:<3} | {item['nama']:<15} | {item['jumlah']:<7} | {item['harga']:<10.2f} | {item['total']:<10.2f} |{RESET}")
            total_payment += item['total']
        print("=" * 60)
        print(f"{CYAN}| {'TOTAL BAYAR':<49} | {total_payment:<10.2f} |{RESET}")
        print("=" * 60)
        print(f"{RED}     Terima kasih telah berbelanja di Saintek Motor!      {RESET}")
        print("=" * 60)
        time.sleep(0.5)  # Delay untuk efek animasi latar belakang berganti

    # Print final receipt after the animation effect
    clear_screen()  # Clear screen before showing the final receipt
    print("\n" + "=" * 60)
    print(f"{MAGENTA}             STRUK BELANJA SAINTEK MOTOR            {RESET}")
    print(f"{CYAN}            {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    print("=" * 60)
    print(f"{YELLOW}| {'No':<3} | {'Nama Barang':<15} | {'Jumlah':<7} | {'Harga':<10} | {'Total':<10} |{RESET}")
    print("=" * 60)
    for i, item in enumerate(cart_items, start=1):
        print(f"{GREEN}| {i:<3} | {item['nama']:<15} | {item['jumlah']:<7} | {item['harga']:<10.2f} | {item['total']:<10.2f} |{RESET}")
        total_payment += item['total']
    print("=" * 60)
    print(f"{CYAN}| {'TOTAL BAYAR':<49} | {total_payment:<10.2f} |{RESET}")
    print("=" * 60)
    print(f"{RED}     Terima kasih telah berbelanja di Saintek Motor!      {RESET}")
    print("=" * 60)
    time.sleep(2)  # Final delay to show the receipt before exiting

# Fungsi utama
def main():
    welcome_animation()
    while True:
        choice = show_menu()
        if choice == '1':
            add_item()
        elif choice == '2':
            show_cart()
        elif choice == '3':
            print("Fitur ubah barang belum tersedia!")
        elif choice == '4':
            print("Fitur hapus barang belum tersedia!")
        elif choice == '5':
            print_receipt()
        elif choice == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")
        input("\nTekan Enter untuk melanjutkan...")
# Fungsi utama
def main():
    welcome_animation()
    while True:
        choice = show_menu()
        if choice == '1':
            add_item()
        elif choice == '2':
            show_cart()
        elif choice == '3':
            print("Fitur ubah barang belum tersedia!")
        elif choice == '4':
            print("Fitur hapus barang belum tersedia!")
        elif choice == '5':
            print_receipt()
            closing_animation()  # Menambahkan animasi penutupan
        elif choice == '6':
            print("Terima kasih! Program selesai.")
            closing_animation()  # Menambahkan animasi penutupan sebelum keluar
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")
        input("\nTekan Enter untuk melanjutkan...")

# Fungsi animasi penutupan dengan pesan terima kasih
def closing_animation():
    closing_message = "Terima kasih telah berbelanja di dealer kami!"
    print(MAGENTA + "\n\nMengucapkan terima kasih..." + RESET)  # Menggunakan ungu untuk pesan awal
    for i in range(len(closing_message) + 1):
        print("\r" + MAGENTA + closing_message[:i] + RESET, end='', flush=True)  # Menggunakan ungu untuk animasi
        time.sleep(0.1)
    print("\n" + MAGENTA + "Kami tunggu kedatangan Anda kembali!" + RESET)  # Menggunakan ungu untuk pesan akhir
    time.sleep(1)  # Memberikan waktu agar efek animasi terlihat sebelum program berakhir



if __name__ == "__main__":
    main()
