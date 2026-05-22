# ========================================================== 
# praktikum 12 materi 2
# Nama  : Yasmin Khoirun Nisa
# NIM : J0403251071
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

def bellman_ford(graph, start):
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relaksasi berulang
    for _ in range(len(graph) - 1):

        for node in graph:

            for neighbor, weight in graph[node].items():

                if distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight
    return distances