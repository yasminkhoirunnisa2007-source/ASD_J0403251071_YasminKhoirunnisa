# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# Nama  : Yasmin Khoirun Nisa
# NIM : J0403251071
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Representasi weighted graph menggunakan dictionary bersarang
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}
# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D
print("Jalur 1: A -> B -> D =", jalur_1)

print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
 print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
# Jawaban: Total bobot jalur A -> B -> D adalah 9 (hasil dari 4 + 5).
# 2. Berapa total bobot jalur A -> C -> D?
# Jawaban: Total bobot jalur A -> C -> D adalah 3 (hasil dari 2 + 1).
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# Jawaban: Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D.
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
# Jawaban: Jalur terpendek tidak selalu ditentukan dari jumlah edge (garis penghubung), paling sedikit karena setiap edge memiliki bobot (weight) yang nilainya bervariasi.
# Bobot ini bisa merepresentasikan jarak, waktu tempuh, atau biaya. Walaupun sebuah jalur melewati lebih banyak node/edge, akumulasi nilai atau total bobotnya bisa saja 
# jauh lebih kecil dan efisien dibandingkan jalur langsung yang bobotnya besar.

