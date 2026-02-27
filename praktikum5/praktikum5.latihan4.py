#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================
# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
    # Base case:
    # Jika panjang string sudah n, cetak hasil
    if len(hasil) == n: 
        print(hasil) 
        return 
    # Recursive case:
    # Tambah "A" lalu lanjut
    kombinasi(n, hasil + "A") 
     # Tambah "B" lalu lanjut
    kombinasi(n, hasil + "B") 
 
 
kombinasi(2)
# Output:
# AA
# AB
# BA
# BB

# Penjelasan jumlah kombinasi:
# Setiap posisi memiliki 2 pilihan (A atau B).
# Jika panjang n, maka total kombinasi = 2^n.
# Untuk n = 2 → 2^2 = 4 kombinasi.