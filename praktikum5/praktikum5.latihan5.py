#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
 
    # Base case:
    # Jika panjang PIN sudah sesuai, cetak hasil
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
 
    # Backtracking:
    # Coba setiap angka (0,1,2) di setiap posisi
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
 
 
buat_pin(3) 
# Penjelasan (tanpa kode pencegahan duplikat):
# Jika ingin mencegah angka yang sama muncul berulang,
# maka sebelum menambahkan angka ke 'hasil',
# perlu dilakukan pengecekan apakah angka tersebut
# sudah ada di dalam 'hasil'.
# Jika sudah ada → cabang dihentikan (pruning).
# Jika belum → lanjutkan rekursi.
# Tanpa pembatasan: 3^3 = 27 kombinasi
# Dengan pembatasan tanpa pengulangan: 3! = 6 kombinasi