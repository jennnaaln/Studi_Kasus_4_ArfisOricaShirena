data_produk = {
    "nama" : "beras",
    "harga" : "17000 per kg",
    "stok" : "70 kg"
}

while True:
    print("Menu Pengelolaan data produk")
    print("1. Tampilkan data produk")
    print("2. Tambahkan data kategori")
    print("3. Ubah data harga")
    print("4. Hapus data kategori")
    print("5. Keluar")

    pilihan = input("Pilih menu(1-5): ")

    if pilihan == "1":
        print("Data Produk")
        print(data_produk)

    elif pilihan == "2":
        data_produk["kategori"] = "sembako"
        print("Data kategori telah ditambahkan")
        print(data_produk)

    elif pilihan == "3":
        data_produk["harga"] = 20000
        print("Harga beras telah diganti")
        print(data_produk)

    elif pilihan == "4":
        data_produk.pop("kategori")
        print("Data kategori telah dihapus")
        print(data_produk)

    else:
        pilihan == "5"
        print("Selesai")
        print("Data produk setelah perubahan: ", data_produk)
        break