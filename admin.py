import json

def lihat_gudang():
    with open('gudang.json') as f:
        return json.load(f)
data = lihat_gudang()

keranjang = []
def tampilkan(data):
    for item in data['gudang']:
        print(f"{item['id']}. {item['nama']} | Harga: {item['harga']}")
        
def tambah_keranjang(id):
    barang = next((item for item in data['gudang'] if item['id'] == id), None)
    if barang:
        jumlah = int(input(f"Masukkan jumlah {barang['nama']} yang ingin ditambahkan: "))
        keranjang.append({'id': barang['id'], 'nama': barang['nama'], 'harga': barang['harga'], 'jumlah': jumlah})
        print(f"{jumlah}x {barang['nama']} berhasil ditambahkan ke keranjang!")
    else:
        print("Barang tidak ditemukan.")

def hitung_total(keranjang):
    total = 0
    for item in keranjang:
        subtotal = item['harga'] * item['jumlah']
        total += subtotal
        print(f"-------------------------------\nBarang: {item['nama']} | Harga: {item['harga']} | Jumlah: {item['jumlah']}\nSubtotal: {subtotal}")
    return total

def lihat_keranjang():
    if len(keranjang) == 0:
        print("Keranjang masih kosong.")
    else:
        total = hitung_total(keranjang)
        print(f"Total: {total}")

def bayar():
    if len(keranjang) == 0:
        print("Anda belum membeli apa-apa.")
    else:
        print("Struk Pembayaran:")
        total = hitung_total(keranjang)
        print(f"Total: {total}")
        print("-------------------------------\nTerima kasih telah berbelanja!")
        keranjang.clear()