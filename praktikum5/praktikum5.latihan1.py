#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 
def pangkat(a, n): 
    # Base case:
    # Jika n == 0, rekursif berhenti dan mengembalikan 1
    # Karena secara matematika a^0 = 1 
    if n == 0: 
        return 1 
    
    # Recursive case:
    # Fungsi memanggil dirinya sendiri dengan n - 1
    # Artinya a^n = a * a^(n-1)
    return a * pangkat(a, n - 1) 

# Alur:
# Pangkat(2,4) = 2x2x2x2 = 16
print(pangkat(2, 4))  # Output: 16 