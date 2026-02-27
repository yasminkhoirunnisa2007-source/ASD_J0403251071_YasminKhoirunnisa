#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning) 
# ========================================================== 
 
def biner_batas(n, batas, hasil="", jumlah_1=0): 
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti 
    if jumlah_1 > batas: 
        return 
 
    # Base case 
    # Jika panjang string sudah n, cetak hasil
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    # Pilih '0' 
    # Tidak menambah jumlah_1 karena yang ditambah adalah 0
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1' 
    # Tambah jumlah_1 karena menambahkan angka 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) 

# Pemanggilan
# Membuat kombinasi biner panjang 4
# dengan jumlah maksimal angka '1' sebanyak 2
biner_batas(4, 2)
