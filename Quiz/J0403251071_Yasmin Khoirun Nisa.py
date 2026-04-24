# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Yasmin Khoirun Nisa
# NIM     : J0403251071
# Kelas   : TPL A2
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}

    with open(nama_file, "r", encoding="utf-8") as file:
        for line in file:
            kode_buku, judul, harga = line.strip().split(",")
            database_buku[kode_buku] = {
                "Judul": judul,
                "Harga": int(harga)
            }

    return database_buku


# 2. LINKED LIST - MANAJEMEN PROMOSI
class Node:
    def __init__(self, judul):
        self.judul = judul
        self.next = None


class LinkedListPromosi:
    def __init__(self):
        self.head = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi"""
        node_baru = Node(judul)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        current = self.head

        if current is None:
            print("Belum ada buku promosi.")
            return

        while current:
            print("Judul Buku:", current.judul)
            current = current.next


# 3. QUEUE - ANTREAN KASIR
class AntreanKasir:
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """Enqueue"""
        self.antrean.append(nama_pelanggan)
        print(nama_pelanggan, "telah ditambahkan ke antrean.")

    def layani_pelanggan(self):
        """Dequeue"""
        if len(self.antrean) == 0:
            print("Antrean kosong!")
            return None

        pelanggan = self.antrean.pop(0)
        print(pelanggan, "sedang dilayani.")
        return pelanggan


# 4. SORTING - INSERTION SORT
def urutkan_transaksi(list_harga):
    for i in range(1, len(list_harga)):
        key = list_harga[i]
        j = i - 1

        while j >= 0 and key < list_harga[j]:
            list_harga[j + 1] = list_harga[j]
            j -= 1

        list_harga[j + 1] = key

    return list_harga


# ==============================================================================
# MAIN PROGRAM
# ==============================================================================
def main():
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)

    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()

    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku")
        print("2. Kelola Daftar Promosi")
        print("3. Kelola Antrean Kasir")
        print("4. Lihat Laporan Penjualan Terurut")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print("\nKatalog Buku:")
            for kode, info in data_buku.items():
                print(kode, "-", info["Judul"], "-", info["Harga"])
