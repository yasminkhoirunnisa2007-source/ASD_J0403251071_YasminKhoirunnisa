#============================================
# Nama   : Yasmin Khoirun Nisa
# NIM    : J0403251071
# Kelas  : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
#============================================
# ===========================================
# Latihan 2 . Implementasi Algoritma Kruskal
# ===========================================

# Definisikan daftar edge dengan format tuple: (bobot, node_asal, node_tujuan)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Urutkan semua edge dari bobot terkecil ke terbesar (Prinsip Greedy)
edges.sort()

# Inisialisasi list kosong untuk menampung edge yang terpilih menjadi MST
mst = []

# Inisialisasi variabel untuk menghitung akumulasi total bobot MST
total_weight = 0

# Gunakan Set untuk mencatat node mana saja yang sudah terhubung
connected = set()

# Lakukan perulangan (looping) untuk memeriksa setiap edge yang sudah diurutkan
for weight, u, v in edges:
    
    # Cek kondisi logika sederhana untuk menghindari cycle:
    # Jika salah satu node (u atau v) belum terhubung ke dalam set, maka aman untuk diambil
    if u not in connected or v not in connected:
        
        # Masukkan edge yang valid ke dalam list MST
        mst.append((u, v, weight))
        
        # Tambahkan bobot edge tersebut ke total bobot
        total_weight += weight
        
        # Masukkan kedua node tersebut ke dalam set connected agar ditandai sebagai 'sudah terhubung'
        connected.add(u)
        connected.add(v)

# Cetak hasil akhir Minimum Spanning Tree (MST)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Cetak total bobot minimum dari keseluruhan MST
print("Total bobot =", total_weight)

# Jawaban Analisis
# 1. Edge mana yang dipilih pertama kali?
#    - Edge ('C', 'D') dengan bobot 1.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    - Karena Kruskal menggunakan prinsip Greedy, yaitu memprioritaskan bobot 
#      paling ringan terlebih dahulu demi mendapatkan total bobot yang paling minimum.

# 3. Berapa total bobot MST yang dihasilkan?
#    - Total bobot = 6 (Hasil penjumlahan dari edge yang terpilih: 1 + 2 + 3).

# 4. Mengapa edge tertentu tidak dipilih?
#    - Edge ('A', 'B') dan ('A', 'D') diabaikan karena semua node (A, B, C, D) 
#      sudah masuk ke dalam set `connected`. Jika edge tersebut dipaksakan masuk, 
#      maka akan terbentuk siklus/looping (cycle) yang melanggar aturan pohon (tree).