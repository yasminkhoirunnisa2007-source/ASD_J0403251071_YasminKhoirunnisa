# =========================================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus Algoritma: Dijkstra
# Nama  : Yasmin Khoirun Nisa
# NIM : J0403251071
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# Jawaban: Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# Jawaban: Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur Gerbang -> Kantin -> Lab -> Aula.
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Jawaban: Jalur langsung tidak selalu menghasilkan jarak paling kecil karena bobot pada setiap edge dapat berbeda. 
# Dalam kasus ini, meskipun ada jalur langsung dari Gerbang ke Aula melalui Kantin, 
# jalur tersebut memiliki bobot yang lebih besar dibandingkan jalur melalui Lab. 
# Oleh karena itu, penting untuk mempertimbangkan bobot pada setiap edge saat menentukan jalur terpendek.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Jawaban: Dijkstra cocok digunakan pada kasus lokasi kampus ini karena graph yang digunakan memiliki bobot positif (waktu tempuh dalam menit) 
# dan kita ingin menemukan jalur terpendek dari satu titik ke titik lainnya. 
# Dijkstra efisien untuk graph dengan bobot positif dan dapat memberikan hasil yang akurat dalam menentukan jalur terpendek.