#============================================
# Nama   : Yasmin Khoirun Nisa
# NIM    : J0403251071
# Kelas  : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
#============================================
# =============================================================
# Latihan 5 . Tugas Mandiri: Buat Program MST dengan Kasus Baru
# =============================================================
# Representasi Weighted Graph (Kasus 1: Jaringan Jalan Antar Kota)
# Format data: (bobot_jarak, kota_asal, kota_tujuan)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Implementasi Algoritma Kruskal
# Urutkan rute jalan berdasarkan jarak terpendek (Prinsip Greedy)
edges.sort()

# List untuk menampung rute jalan utama terpilih (MST)
mst = []

# Variabel akumulasi total jarak minimum
total_weight = 0

# Set untuk mencatat kota yang sudah terhubung
connected = set()

# Perulangan untuk memeriksa setiap rute jalan hasil pengurutan
for weight, u, v in edges:
    # Jika salah satu kota belum terhubung, rute aman diambil (no cycle)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Output MST & 4. Output Total Bobot Minimum
print("Minimum Spanning Tree (Rute Jalan Utama Terpilih):")
for edge in mst:
    print(f"- {edge[0]} ke {edge[1]} dengan bobot: {edge[2]}")

print("\nTotal bobot =", total_weight)


# JAWABAN ANALISIS
# 1. Kasus apa yang dipilih?
#    - Kasus 1 (Jaringan Jalan Antar Kota).

# 2. Algoritma apa yang digunakan?
#    - Algoritma Kruskal.

# 3. Edge mana saja yang dipilih dalam MST?
#    - Bogor - Depok (2), Depok - Jakarta (3), dan Depok - Bandung (4).

# 4. Berapa total bobot MST?
#    - Total bobotnya adalah 9.

# 5. Mengapa edge tertentu tidak dipilih?
#    - Karena semua kota sudah saling terhubung. Jika rute lain dimasukkan,
#       hanya akan membentuk siklus (cycle) memutar yang tidak efisien.