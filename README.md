Ini adalah program kasir untuk memilih, menambah barang, menghitung total dan memberikan struk-like teks kepada user

### Cara Kerja dari Program ini:

1. **Mulai**: Program akan menampilkan pesan selamat datang.

2. **Tampilkan Menu**: Program menampilkan menu utama dengan opsi:
   - **1. Lihat Barang**
   - **2. Lihat Keranjang**
   - **3. Bayar**

3. **Pilih Menu**:
   - **Jika memilih "1" (Lihat Barang)**:
     - Fungsi `tampilkan(data)` akan dipanggil untuk menampilkan daftar barang yang tersedia.
     - Program meminta ID barang untuk ditambahkan ke keranjang.
     - Jika ID tidak valid, program menampilkan pesan error.
     - Jika ID valid, program menjalankan fungsi `tambah_keranjang(id)`:
       - Program akan minta jumlah barang yang diinginkan dari pengguna.
       - Kemudian menambahkan barang ke dalam keranjang.
       - Ini akan di ulangi sampai pengguna memasukkan "0" untuk kembali ke menu utama.

   - **Jika memilih "2" (Lihat Keranjang)**:
     - Fungsi `lihat_keranjang()`akan dipanggil dan menampilkan:
       - Jika keranjang kosong, print pesan bahwa keranjang kosong.
       - Jika ada barang, hitung dan print setiap barang dalam keranjang dan total harga dari semua barang itu.

   - **Jika memilih "3" (Bayar)**:
     - Panggil fungsi `bayar()`:
       - Jika keranjang kosong, print pesan bahwa belum ada barang yang dibeli.
       - Jika ada barang, print struk pembayaran, hitung total dan kosongkan keranjang.
     - Dan Program akan berhenti setelah memilih ini.

   - **Jika pilihan tidak valid**: Pesan error akan diprint dan kembali ke menu.

4. **Selesai**

