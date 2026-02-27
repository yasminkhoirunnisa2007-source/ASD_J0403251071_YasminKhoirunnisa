#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0): 
 
    # Base case 
    # Jika index sudah di elemen terakhir,
    # kembalikan nilai elemen tersebut
    if index == len(data) - 1: 
        return data[index] 
 
    # Recursive case
    # Recursive call:
    # Cari nilai maksimum dari sisa list (index + 1)
    maks_sisa = cari_maks(data, index + 1) 
     # Bandingkan elemen sekarang dengan hasil dari sisa list
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 
 
 
angka = [3, 7, 2, 9, 5] 
# Alur:
# Fungsi mengecek dari depan,
# lalu membandingkan tiap elemen dengan maksimum dari sisa list.
# Proses berhenti saat elemen terakhir (base case),
# lalu hasil dibandingkan saat kembali (unwinding).
# Hasil akhir = 9

print("Nilai maksimum:", cari_maks(angka)) 