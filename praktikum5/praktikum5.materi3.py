#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ========================================================== 
def jumlah_list(data, index=0): 
    # Base case: jika index sudah mencapai panjang list,
    # berarti semua elemen sudah dijumlahkan -> berhenti
    if index == len(data): 
        return 0 
    
    # Recursive case: elemen sekarang + jumlah elemen setelahnya 
    return data[index] + jumlah_list(data, index + 1) 

# Alur jumlah_list([2,4,6,8]):
# 2 + 4 + 6 + 8 + 0 = 20
print(jumlah_list([2, 4, 6, 8]))  # Output: 20