class Produk:
    def __init__(self, kode, nama, stok, harga):
        self.kode = kode
        self.nama = nama
        self.stok = stok
        self.harga = harga

    def tambah_stok(self, jumlah):
        self.stok += jumlah
        print(f"{jumlah} unit {self.nama} telah ditambahkan ke stok.")
    
    def kurangi_stok(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
            print(f"{jumlah} unit {self.nama} telah dikeluarkan dari stok.")
        else:
            print(f"Stok {self.nama} tidak cukup untuk melakukan pengeluaran.")

    def tampilkan_info(self):
        print(f"Kode: {self.kode}")
        print(f"Nama: {self.nama}")
        print(f"Stok: {self.stok}")
        print(f"Harga: {self.harga}")
        print("------------------------------")


class Gudang:
    def __init__(self):
        self.produk_list = []

    def tambah_produk(self, produk):
        self.produk_list.append(produk)
        print(f"Produk {produk.nama} telah ditambahkan ke gudang.")

    def cari_produk(self, kode):
        for produk in self.produk_list:
            if produk.kode == kode:
                return produk
        return None

    def tampilkan_semua_produk(self):
        if len(self.produk_list) == 0:
            print("Gudang kosong.")
        else:
            for produk in self.produk_list:
                produk.tampilkan_info()


def menu():
    print("Selamat datang di sistem manajemen produk gudang!")
    print("1. Tambah produk")
    print("2. Cari produk")
    print("3. Tambah stok produk")
    print("4. Kurangi stok produk")
    print("5. Tampilkan semua produk")
    print("6. Keluar")


def main():
    gudang = Gudang()

    while True:
        menu()
        pilihan = input("Pilih menu (1/2/3/4/5/6): ")

        if pilihan == "1":
            kode = input("Masukkan kode produk: ")
            nama = input("Masukkan nama produk: ")
            stok = int(input("Masukkan jumlah stok: "))
            harga = float(input("Masukkan harga produk: "))
            produk = Produk(kode, nama, stok, harga)
            gudang.tambah_produk(produk)
        
        elif pilihan == "2":
            kode = input("Masukkan kode produk yang ingin dicari: ")
            produk = gudang.cari_produk(kode)
            if produk:
                produk.tampilkan_info()
            else:
                print("Produk tidak ditemukan.")

        elif pilihan == "3":
            kode = input("Masukkan kode produk untuk menambah stok: ")
            produk = gudang.cari_produk(kode)
            if produk:
                jumlah = int(input(f"Berapa banyak {produk.nama} yang ingin ditambahkan? "))
                produk.tambah_stok(jumlah)
            else:
                print("Produk tidak ditemukan.")
        
        elif pilihan == "4":
            kode = input("Masukkan kode produk untuk mengurangi stok: ")
            produk = gudang.cari_produk(kode)
            if produk:
                jumlah = int(input(f"Berapa banyak {produk.nama} yang ingin dikeluarkan? "))
                produk.kurangi_stok(jumlah)
            else:
                print("Produk tidak ditemukan.")

        elif pilihan == "5":
            gudang.tampilkan_semua_produk()
        
        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem manajemen produk!")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
