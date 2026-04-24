# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Yasmin Khoirun Nisa
# NIM     : J0403251071
# Kelas   : TPL A2
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(buku.txt):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {buku.txt: {}} # Inisialisasi dictionary untuk menyimpan data buku
    # TODO: Implementasikan kode pembacaan file di sini
    with open("Buku.txt", "r", encoding="utf-8") as file: # Membaca file
        for line in file: # Iterasi setiap baris
            kode_buku, judul, harga = line.strip().split(",")
            database_buku[kode_buku] = {"Judul": judul, "Harga": int(harga)}
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self):
         self.head = None
         

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        node_baru = Node(judul)
        if self.head is None:
            self.head = node_baru
        else:
            # Menambahkan di akhir linked list
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node_baru

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        current = self.head
        while current is not None:
            print("Judul Buku:", current.judul)
            current = current.next

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        # TODO: Implementasikan prinsip FIFO
        self.antrean.append(nama_pelanggan) # Menambahkan pelanggan ke antrean

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        # TODO: Implementasikan prinsip FIFO
        if self.antrean:
            pelanggan_dilayani = self.antrean.pop(0)
            print("Melayani pelanggan:", pelanggan_dilayani)
        else:
            print("Antrean kosong.")
        pass

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    # TODO: Implementasikan algoritma sorting secara manual
    def insertion_sort(data): 
    # Loop mulai dari elemen kedua 
        for i in range(1, len(data)): 
 
            key = data[i]   # Simpan nilai yang akan disisipkan 
            j = i - 1       # Indeks elemen terakhir di bagian kiri 
 
        # Geser elemen yang lebih besar dari key 
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
 
        # Sisipkan key ke posisi yang benar 
        data[j + 1] = key
    return data

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:", data_buku)
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            nama = input("Nama Pelanggan: ")
            antrean_toko.tambah_antrean(nama)
            # Tambahkan logika untuk melayani jika diperlukan

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()