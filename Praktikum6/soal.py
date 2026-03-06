#============================================================
# Nama: Yasmin Khoirun Nisa
# NIM: J0403251071
# Kelas: TPL A2
# LATIHAN SOAL PENGURUTAN
#============================================================
# Menggunakan Bubble Sort

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

print("Data awal :", data)

n = len(data)

# Bubble Sort Descending
for i in range(n-1):
    for j in range(n-1-i):
        if data[j] < data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Data setelah diurutkan (descending):", data)

# Mengambil 5 nilai tertinggi
lima_tertinggi = data[:5]

print("5 nilai tertinggi:", lima_tertinggi)
print("Jumlah kandidat yang lolos:", len(lima_tertinggi))
