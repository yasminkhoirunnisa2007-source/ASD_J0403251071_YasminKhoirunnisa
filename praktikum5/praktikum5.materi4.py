#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ========================================================== 
def biner(n, hasil=""): 
    # Base case: jika panjang string sudah n, cetak hasil lalu berhenti
    if len(hasil) == n: 
        print(hasil) 
        return
  # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") 
 
    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1") 
# Memanggil fungsi untuk n = 3
# Akan menghasilkan semua kombinasi biner sepanjang 3 digit
biner(3) 