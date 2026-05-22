# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford
# Nama  : Yasmin Khoirun Nisa
# NIM : J0403251071
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
# jawaban: Bobot langsung dari A ke B adalah 5.
# 2. Berapa total bobot jalur A -> C -> B?
# jawaban: Total bobot jalur A -> C -> B adalah 2 (hasil dari 4 + (-2)).
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# jawaban: Jalur yang menghasilkan jarak lebih kecil menuju B adalah jalur A -> C -> B.
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# jawaban: Karena Bellman-Ford tidak langsung mengunci nilai jarak suatu node (tidak greedy seperti Dijkstra). 
# Algoritma ini mengulang pengecekan ke seluruh edge sebanyak V-1 kali, sehingga perubahan bobot akibat nilai negatif akan selalu terhitung di perulangan berikutnya.
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# jawaban: Relaksasi edge adalah proses mengecek dan memperbarui jarak ke suatu node tetangga jika ditemukan rute baru yang total bobotnya lebih kecil/murah.
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# jawaban: Dijkstra lebih cepat (menggunakan priority queue) tapi gagal pada bobot negatif. 
# Bellman-Ford lebih lambat (mengecek semua edge berulang-ulang) tapi aman untuk bobot negatif dan bisa mendeteksi negative cycle.
