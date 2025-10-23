import sys # Membantu dalam men-debug dan mengelola perilaku tingkat sistem dalam skrip Python.

# Nama Tempat Usaha
tempat_kami = "Warkop Madura"

# Barang yang ada di menu saat ini
barang = [[1,"Ikan_Goreng", 20000], [2,"Espresso", 15000], [3,"Milk Tea"
        , 10000], [4,"Kopi Hitam", 5000]]

print(f"Selamat datang di {tempat_kami}! Berikut menu yang kami tawarkan:")

# Membuat fungsi untuk menampilakan barang di menu
def list_barang():
    for data in barang:
        index = data[0]
        nama = data[1]
        harga = data[2]
        print(f"{index}.{nama}:\t Rp{harga}")

# Menampilkan barang di menu
list_barang()

# Sebagai penyimpanan jika ada pembeli yang membeli barang
barang_beli = []

# Proses looping untuk mengecek jika pembeli masih ingin membeli atau tidak.
while True:
    # Memberikan pilihan untuk pembeli membeli barang
    try:
        user_beli = int(input("Anda ingin membeli apa baginda?\t").strip())
    except Exception as e:
        print(f"Ada error di sini: {e}")
        sys.exit()
    # Menghapus satu baris
    sys.stdout.write("\033[F") 
    sys.stdout.write("\033[K")  
    sys.stdout.flush()

    indices = [item[0] for item in barang]

    # Jika barang tidak ada di menu barnag maka tampilkan Pesan Di bawah:
    if user_beli not in indices:
        print(f"Harap pilih menu yang ada")
    else:
        # Jika ada maka tampilkan apa yang dipilih, dan tambahkan barang itu ke list barang_beli
        for item in barang:
            if item[0] == user_beli:
                nama, harga = item[1], item[2]
                print(f"\nAnda memilih {nama} seharga Rp{harga}.")
                barang_beli.append({"nama": nama, "harga": harga})
                break  

        # Membuat kondisi jika pembeli ingin stop belanja, dan melakukan transaksi.
        lanjut = input("Apa anda masih ingin lanjut membeli? (y/n)")
        if lanjut.lower() == "n":
            break
        elif lanjut.lower() != "y":
            print(f"Anda ingin melakukan apa? input lagi")

# Menampilkan struct belanjaan dan menghitung total biaya
total = 0
for i, item in enumerate(barang_beli, start=1):
    print(f"{i}. {item['nama']} - Rp{item['harga']}")
    total += item['harga']

print(f"\nTotal belanja anda: Rp{total}")
print("Sampai jumpa lagi, Baginda! Jangan lupa untuk datang ke caffe kami!")
