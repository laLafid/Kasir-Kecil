import admin as ad
data = ad.lihat_gudang()

print("Selamat Datang di Toko Lafid!")

while True:
    print("Menu:")
    print("1. Lihat Lihat\n2. Lihat Keranjang\n3. Bayar")
    menu = input("Pilih menu: ")
    if menu == '1':
        ad.tampilkan(data)
        while True:
            id = int(input("Masukkan ID barang untuk ditambah ke keranjang (0 untuk kembali): "))
            if id == 0:
                break
            ad.tambah_keranjang(id)
    elif menu == '2':
        ad.lihat_keranjang()
    elif menu == '3':
        ad.bayar()
        break
    else:
        print("Pilihan tidak valid")