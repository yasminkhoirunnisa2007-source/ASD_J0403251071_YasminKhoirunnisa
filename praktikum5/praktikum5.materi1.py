#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Contoh Rekursi 1: Faktorial 
# ========================================================== 
def faktorial(n): 
    # Base case: berhenti ketika n = 0 
    # Jika n = 0, rekursi berhenti dan mengembalikan 1
    # (Karena 0!= 1)
    if n == 0: 
        return 1 
    # Recursive case: masalah diperkecil menjadi faktorial(n-1)
    # Fungsi memanggil dirinya sendiri dengan nilai(n - 1) 
    # Untuk memperkecil masalah
    # Hasil akhirnya adalah n dikali dengan faktorial (n - 1)
    return n * faktorial(n - 1) 
# Faktorial(5) = 5x4x3x2x1 = 120
print(faktorial(5))  # Output: 120
