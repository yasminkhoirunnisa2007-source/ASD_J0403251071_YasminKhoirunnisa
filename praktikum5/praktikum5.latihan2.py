#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ========================================================== 
 
def countdown(n): 
 
    # Base case: berhenti saat n == 0
    if n == 0: 
        print("Selesai") 
        return 
    # Fase stacking (masuk dan ditumpuk dulu)
    print("Masuk:", n) 
    # Pemanggilan rekursif
    countdown(n - 1) 
    # Fase unwinding (keluar satu per satu setelah selesai)
    # Output "Keluar" muncul terbalik karena rekursif
    # Menggunakan sistem stack (LIFO: Last In First Out)
    # Sehingga yang terakhir masuk akan pertama keluar
    print("Keluar:", n) 
 
 
countdown(3)
# Urutan output:
# Masuk: 3
# Masuk: 2
# Masuk: 1
# Selesai
# Keluar: 1
# Keluar: 2
# Keluar: 3