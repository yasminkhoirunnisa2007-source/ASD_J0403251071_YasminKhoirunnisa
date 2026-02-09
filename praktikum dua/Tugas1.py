#================================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File . txt)

# Nama  : Yasmin Khoirun Nisa
# NIM   : J0403251071
# Kelas : A/P2
#=================================================================


#==================================================================
# Konstanta nama file
#==================================================================
nama_file = "stock_barang.txt"


#==================================================================
# Fungsi: Membaca data dari file
#==================================================================
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok

    Output:
    - stok_dict (dictionary)
      key = Kodebarang
      value ={"Nama Barang": namabarang, "stok": stok}
    """
    stok_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kodebarang, namabarang, stok = baris.split(",")     
            stok_dict[kodebarang] = {
                "Nama Barang": namabarang,
                "Stok": int(stok)}
    return stok_dict
        
buka_stok = baca_stok(nama_file) 
print ("jumlah data terbaca", len(buka_stok))


#==================================================================
# Fungsi: Menyimpan data ke file
#==================================================================
def simpan_data(nama_file,stok_dict):
    """
    Menyimpan Seluruh data stok ke file teks.
    format per baris : KodeBarang,NamaBarang,Stok

    Output:
    - stok_dict (dictionary)
      key = kodebarang
      value = {"nama": namabarang, "stok": stok}
    """
    
    with open(nama_file, "w", encoding="utf-8") as file:
        for kodebarang in sorted(stok_dict.keys()):
            namabarang = stok_dict[kodebarang]["Nama Barang"]
            stok = stok_dict[kodebarang]["Stok"]
            file.write(f"{kodebarang},{namabarang},{stok}\n")

    print("\nData Berhasil Disimpan Ke File :", nama_file)

#==================================================================
# Fungsi: Menampilkan semua data
#==================================================================
def tampilkan_stok(stok_dict):
    print("\n=== STOCK BARANG ===")
    print(f"{'Kode Barang':<10} | {'Nama Barang':<12} | {'Stok':>5}")
    print("-"*32)

    for kodebarang in sorted(stok_dict.keys()):
        namabarang = stok_dict[kodebarang]["Nama Barang"]
        stok = stok_dict[kodebarang]["Stok"]
        print(f"{kodebarang:<10} | {namabarang:<12} | {stok:>5}")

tampilkan_stok(buka_stok)


#==================================================================
# Fungsi: Cari barang berdasarkan kode
#==================================================================
def cari_barang(stok_dict):
    cari_kodebarang = input("Masukkan kode barang yang ingin dicari:").strip()

    if cari_kodebarang in stok_dict:
        namabarang = stok_dict[cari_kodebarang]["Nama Barang"]
        stok = stok_dict[cari_kodebarang]["Stok"]

        print("/n=== Data Barang Ditemukan ===")
        print(f"Kode Barang : {cari_kodebarang}")
        print(f"Nama Barang : {namabarang}")
        print(f"Stok    : {stok}")

    else:
        print("Data tidak ditemukan. Pastikan Kode Barang yang dimasukan benar")
    
cari_barang(buka_stok)


#==================================================================
# Fungsi: Tambah barang baru
#==================================================================
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru:").strip()

    # validasi kode tidak boleh duplikat
    if kode in stok_dict:
        print("Kode barang sudah digunakan!. Pastikan masukkan kode yang belum pernah digunakan")
        return
    nama = input("Masukan nama barang:").strip()

    try:
        stok_awal = int(input("Masukkan stok awal:"))
        if stok_awal < 0:
            print("Stok tidak boleh negatif!")
            return
    except ValueError:
        print("Stok harus berupa angka!")
        return
    
    # Menyimpan ke dictionary
    stok_dict[kode] = {
        "Nama Barang": nama,
        "Stok": stok_awal
    }
    print("Barang baru berhasil ditambahkan")
    
tambah_barang(buka_stok)

#==================================================================
# Fungsi: Update stok barang
#==================================================================
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    # Mengecek apakah kode ada
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan!")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    stok_sekarang = stok_dict[kode]["Stok"]

    if pilihan == "1":
        stok_dict[kode]["Stok"] = stok_sekarang + jumlah
        print("Stok berhasil ditambahkan")

    elif pilihan == "2":
        if stok_sekarang - jumlah < 0:
            print("Stok tidak boleh menjadi negatif!")
            return
        stok_dict[kode]["Stok"] = stok_sekarang - jumlah
        print("Stok berhasil dikurangi")

    else:
        print("Pilihan tidak valid!")
        return
    
update_stok(buka_stok)

#==================================================================
# Fungsi: Program Utama
#==================================================================
def main():
    # Membaca data otomatis saat program dimulai
    buka_stok = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang Berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_stok(buka_stok) #memanggil fs 2 menampilkan data

        elif pilihan == "2":            #memanggil fs.3 mencari data
            cari_barang(buka_stok)

        elif pilihan == "3":             #memanggil fs.4 tambah  data
            tambah_barang(buka_stok)

        elif pilihan == "4" :                    #memanggil fs.5 menyimpan data ke file
            update_stok(buka_stok)

        elif pilihan == "5" :
            simpan_data(nama_file,buka_stok)
    
        elif pilihan == "0":
            print("Program Selesai.")
            break

        else:
            print("kesalahan")
# Menjalankan program utama
if __name__ == "__main__":
    main()