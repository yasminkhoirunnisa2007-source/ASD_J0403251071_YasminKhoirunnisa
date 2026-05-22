# ========================================================== 
# Latihan 2: Implementasi Dijkstra
# Nama  : Yasmin Khoirun Nisa
# NIM : J0403251071
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# jawaban: Jarak terpendek dari A ke B adalah 4.
# 2. Berapa jarak terpendek dari A ke C?
# Jawaban: Jarak terpendek dari A ke C adalah 2.
# 3. Berapa jarak terpendek dari A ke D?
# Jawaban: Jarak terpendek dari A ke D adalah 3.
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Jawaban: Karena total akumulasi bobot rute lewat C jauh lebih kecil. Jika lewat C (A -> C -> D), 
# bobotnya hanya 3 (2 + 1). Sedangkan jika lewat B (A -> B -> D), total bobotnya mencapai 9 (4 + 5).
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Jawaban: Fungsi priority_queue adalah untuk menyimpan dan mengurutkan pasangan (jarak, node)
# secara otomatis mulai dari jarak yang paling kecil. 
# Ini memungkinkan algoritma selalu mengambil (heappop) rute yang paling efisien terlebih dahulu untuk diproses.
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Jawaban: Dijkstra tidak cocok untuk bobot negatif karena menggunakan prinsip "greedy".
# Sekali suatu node selesai diproses dan dianggap memiliki jarak terpendek, nilainya sudah "final" dan tidak akan ditinjau ulang. 
# Adanya bobot negatif bisa membuat rute yang lebih panjang di awal menjadi lebih murah di akhir, 
# yang mana tidak terdeteksi oleh Dijkstra dan berpotensi memicu hasil yang keliru atau loop tak berujung.