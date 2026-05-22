# ========================================================== 
# Latihan 5. Studi Kasus dengan Program Shortest Path
# Nama  : Yasmin Khoirun Nisa
# NIM : J0403251071
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

import heapq

# 1. Representasi graph berbobot menggunakan dictionary bersarang
# Sesuai data: 
# Bogor -> Jakarta = 5, Bogor -> Depok = 2
# Depok -> Jakarta = 2, Depok -> Bandung = 6
# Jakarta -> Bandung = 7
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Menginisialisasi semua jarak ke node lain dengan nilai tak hingga (inf)
    distances = {node: float('inf') for node in graph}
    # Jarak dari node asal ke dirinya sendiri selalu 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        # Mengambil node dengan bobot/jarak terkecil dari queue
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak yang baru diambil lebih besar dari jarak yang sudah tercatat, skip
        if current_distance > distances[current_node]:
            continue
            
        # Memeriksa semua kota tetangga dari kota saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan rute/jarak yang lebih pendek, perbarui datanya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# 3. Input node awal (Penentuan node awal dalam program)
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# 4. Output jarak terpendek dari node awal ke semua node
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# jawaban: Node awal yang digunakan adalah 'Bogor'.
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# jawaban: Node dengan jarak terkecil dari 'Bogor' adalah 'Depok' dengan jarak 2.
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# jawaban: Node dengan jarak terbesar dari 'Bogor' adalah 'Bandung' dengan jarak 8.
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# jawaban: Cara kerja algoritma Dijkstra pada kasus ini:
#    - Algoritma mulai dari 'Bogor' (jarak = 0), sementara kota lain diatur ke tak hingga (inf).
#    - Dari 'Bogor', tetangganya diperiksa: 'Jakarta' (jarak 5) dan 'Depok' (jarak 2).
#    - Karena 'Depok' punya jarak terkecil (2), algoritma lanjut memeriksa tetangga dari 'Depok', yaitu 'Jakarta' dan 'Bandung'.
#    - Jalur Bogor -> Depok -> Jakarta menghasilkan jarak 4 (2 + 2). Karena 4 lebih kecil dari rute langsung Bogor -> Jakarta (5), jarak ke 'Jakarta' diperbarui menjadi 4.
#    - Jalur Bogor -> Depok -> Bandung menghasilkan jarak 8 (2 + 6).
#    - Terakhir, dari 'Jakarta' diperiksa rute ke 'Bandung' (4 + 7 = 11). Karena 11 lebih besar dari rute lewat Depok (8), jarak ke 'Bandung' tetap bertahan di angka 8. Proses selesai karena semua jalur telah dievaluasi.
