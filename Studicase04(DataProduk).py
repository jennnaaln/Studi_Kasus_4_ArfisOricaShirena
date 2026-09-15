# dictionary data produk yang berisi key nama, harga, dan stok 
data_produk = {
    "nama" : "beras",
    "harga" : "17000 per kg",
    "stok" : "70 kg"
}

# Menggunakan perulangan while untuk menampilkan beberapa menu pengelolaan data 
while True:
    print("Menu Pengelolaan data produk")
    print("1. Tampilkan data produk")
    print("2. Tambahkan data kategori")
    print("3. Ubah data harga")
    print("4. Hapus data kategori")
    print("5. Keluar")

    pilihan = input("Pilih menu(1-5): ")

# jika user memilih menu 1 makan data produk ouput akan menampilkan data sekarang
    if pilihan == "1":
        print("Data Produk")
        print(data_produk)

# Jika user memilih menu 2 maka akan menambah data baru yaitu data kategori ke dalam data produk
    elif pilihan == "2":
        data_produk["kategori"] = "sembako"
        print("Data kategori telah ditambahkan")
        print(data_produk)

# Jika user memilih menu 3 maka akan mengganti harga dari 17000 menjadi 20000 di dalam data produk
    elif pilihan == "3":
        data_produk["harga"] = 20000
        print("Harga beras telah diganti")
        print(data_produk)

# Jika user memilih menu 4 maka akan menghapus data kategori dalam data produk
    elif pilihan == "4":
        data_produk.pop("kategori")
        print("Data kategori telah dihapus")
        print(data_produk)

# Jika user memilih menu 5 maka program akan selesai dan akan menampilkan data produk setelh perubahan
    else:
        pilihan == "5"
        print("Selesai")
        print("Data produk setelah perubahan: ", data_produk)
        break
