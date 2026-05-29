#============================================
# Nama   : Yasmin Khoirun Nisa
# NIM    : J0403251071
# Kelas  : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
#============================================
# ===========================================
# Latihan 1 . Memahami Konsep Spanning Tree
# ===========================================

# Daftar edge graph awal berdasarkan gambar
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid (menghubungkan semua node tanpa cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan daftar edge pada graph awal
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan contoh spanning tree yang valid
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge pada graph awal dan spanning tree
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    - Graph awal: Bisa memiliki siklus (cycle) dan jumlah edge lebih banyak.
#    - Spanning tree: Subgraph terhubung yang wajib mencakup semua node, 
#      tetapi tidak boleh memiliki siklus sama sekali.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    - Karena definisi dasar dari sebuah "tree" (pohon) dalam teori graph 
#      adalah graph terhubung yang bebas dari siklus (acyclic).

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    - Karena untuk menghubungkan V node tanpa membentuk siklus, hanya 
#      diperlukan tepat (V - 1) edge. Penambahan edge dari jumlah itu 
#      pasti akan menciptakan siklus pada graph.