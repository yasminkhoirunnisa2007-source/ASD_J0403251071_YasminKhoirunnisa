#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 
def hitung(n): 
    # Base case berhenti saat n == 0
    if n == 0: 
        print("Selesai") 
        return 
    
    print("Masuk:", n)    # fase stacking (sebelum rekursif/masuk ke fungsi lagi)
    hitung(n - 1)         # pemanggilan rekursif (memperkecil masalah)
    print("Keluar:", n)   # fase unwinding (setelah rekursif selesai/keluar bertahap)

hitung(3) 
# Urutan output:
# Masuk: 3
# Masuk: 2
# Masuk: 1
# Selesai
# Keluar: 1
# Keluar: 2
# Keluar: 3
