#============================================
# Nama   : Yasmin Khoirun Nisa
# NIM    : J0403251071
# Kelas  : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
#============================================
import heapq

# Definisikan graph menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    
    # Masukkan semua edge dari node awal ke dalam min-heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Masukkan edge baru dari node yang baru dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan fungsi Prim dimulai dari node 'A'
mst, total = prim(graph, 'A')

# Menampilkan hasil
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} dengan bobot {edge[2]}")
    
print("Total bobot =", total)