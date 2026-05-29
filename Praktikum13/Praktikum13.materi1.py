#============================================
# Nama   : Yasmin Khoirun Nisa
# NIM    : J0403251071
# Kelas  : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
#============================================
# ==========================================================
# Implementasi Algoritma Kruskal
# ==========================================================

# Definisikan daftar edge (sisi) dalam bentuk tuple: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Urutkan semua edge berdasarkan bobotnya secara ascending (dari terkecil ke terbesar)
# Ini adalah ciri khas algoritma Kruskal (pendekatan greedy)
edges.sort()

# Inisialisasi list untuk menampung hasil MST dan variabel untuk total bobot
mst = []
total_weight = 0

# Inisialisasi set untuk mencatat node/simpul yang sudah terhubung
connected = set()

# Iterasi (looping) melalui setiap edge yang sudah diurutkan
for weight, u, v in edges:
    
    # Cek kondisi logika: jika salah satu atau kedua node belum masuk ke dalam set 'connected',
    # maka edge ini aman diambil dan tidak membentuk cycle (siklus) sederhana.
    if u not in connected or v not in connected:
        
        # Masukkan edge ke dalam daftar Minimum Spanning Tree (MST)
        mst.append((u, v, weight))
        
        # Tambahkan bobot edge ini ke total bobot MST
        total_weight += weight

        # Masukkan kedua node (u dan v) ke dalam set 'connected' agar ditandai sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil Minimum Spanning Tree (MST) ke layar
print("Minimum Spanning Tree:")
for edge in mst:
    # Menampilkan edge dengan format yang lebih rapi (Node1 - Node2 : Bobot)
    print(f"{edge[0]} - {edge[1]} dengan bobot {edge[2]}")
    
# Menampilkan total bobot keseluruhan dari MST yang terbentuk
print("Total bobot =", total_weight)