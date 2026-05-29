#============================================
# Nama   : Yasmin Khoirun Nisa
# NIM    : J0403251071
# Kelas  : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
#============================================
# ===========================================
# Latihan 3 . Implementasi Algoritma Prim
# ===========================================
import heapq

# Representasi Graph menggunakan Dictionary bertingkat (Adjacency List beserta Bobotnya)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi utama Algoritma Prim untuk mencari Minimum Spanning Tree
def prim(graph, start):
    # Set untuk mencatat node mana saja yang sudah dikunjungi/masuk ke dalam MST
    visited = set([start])
    
    # Priority Queue (Min-Heap) untuk menyimpan dan mengurutkan edge berdasarkan bobot terkecil
    edges = []
    
    # Masukkan semua edge tetangga yang terhubung langsung dengan node awal ke dalam heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    # List untuk menampung hasil akhir edge MST
    mst = []
    # Variabel akumulator total bobot MST
    total_weight = 0
    
    # Melakukan perulangan selama priority queue 'edges' tidak kosong
    while edges:
        # Ambil edge dengan bobot paling kecil menggunakan heap pop
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan (v) belum pernah dikunjungi, maka aman diambil (menghindari cycle)
        if v not in visited:
            # Tandai node tujuan (v) sebagai node yang sudah dikunjungi
            visited.add(v)
            
            # Masukkan edge valid tersebut ke dalam list hasil MST
            mst.append((u, v, weight))
            # Tambahkan bobotnya ke total akumulasi
            total_weight += weight
            
            # Memeriksa semua tetangga dari node yang baru saja dikunjungi (v)
            for neighbor, w in graph[v].items():
                # Jika tetangga tersebut belum dikunjungi, masukkan edge baru tersebut ke dalam heap
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    # Mengembalikan hasil list MST beserta akumulasi total bobotnya
    return mst, total_weight

# Eksekusi fungsi Prim dimulai dari node awal 'A'
mst, total = prim(graph, 'A')

# Cetak output hasil pencarian MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis 

# 1. Node awal apa yang digunakan?
#    - Node 'A' (sesuai parameter pemanggilan fungsi `prim(graph, 'A')`).

# 2. Edge mana yang dipilih pertama kali?
#    - Edge ('A', 'C') dengan bobot 2, karena merupakan bobot terkecil dari node 'A'.

# 3. Bagaimana Prim menentukan edge berikutnya?
#    - Dengan memeriksa semua edge yang terhubung ke node-node yang telah dikunjungi (visited), 
#      lalu memilih edge dengan bobot terkecil di Min-Heap yang menuju ke node yang belum dikunjungi.

# 4. Berapa total bobot MST yang dihasilkan?
#    - Total bobot = 6 (Hasil penjumlahan dari edge yang terpilih: 2 + 1 + 3).

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Prim: Membangun MST secara berurutan dan bertahap dari satu node acuan (tumbuh dari dalam).
#    - Kruskal: Memilih edge berdasarkan bobot global terkecil di seluruh graph tanpa terikat 
#      pada satu node awal (menggabungkan komponen terpisah menjadi satu pohon tunggal).