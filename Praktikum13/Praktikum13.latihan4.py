#============================================
# Nama   : Yasmin Khoirun Nisa
# NIM    : J0403251071
# Kelas  : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
#============================================
# =====================================================
# Latihan 4. Studi Kasus: Jaringan Kabel Antar Gedung
# ======================================================

# Representasi Weighted Graph berdasarkan data hubungan gedung
# Format data: (biaya, gedung_1, gedung_2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan jalur kabel berdasarkan biaya termurah (Greedy Approach)
edges.sort()

# Inisialisasi list untuk menampung jalur kabel terpilih (MST)
mst_kabel = []

# Inisialisasi variabel untuk menghitung akumulasi total biaya minimum
total_biaya = 0

# Set untuk mencatat gedung mana saja yang sudah terhubung jaringan kabel
connected_gedung = set()

# Proses pemilihan jalur menggunakan logika algoritma Kruskal
for biaya, u, v in edges:
    
    # Periksa apakah salah satu gedung belum terhubung jaringan kabel
    # Ini adalah pengecekan sederhana untuk menghindari terbentuknya siklus (cycle)
    if u not in connected_gedung or v not in connected_gedung:
        
        # Masukkan jalur kabel terpilih ke dalam list MST
        mst_kabel.append((u, v, biaya))
        
        # Tambahkan biaya pemasangan kabel ke total akumulasi biaya
        total_biaya += biaya
        
        # Tandai kedua gedung tersebut sebagai gedung yang sudah terhubung
        connected_gedung.add(u)
        connected_gedung.add(v)

# Menampilkan output hasil perencanaan jaringan kabel antar gedung
print("Jalur kabel yang dipilih untuk dibangun:")
for jalur in mst_kabel:
    print(f"- Jaringan dari {jalur[0]} ke {jalur[1]} dengan biaya: {jalur[2]}")

print(f"\nTotal biaya minimum pemasangan kabel = {total_biaya}")

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    - Algoritma Kruskal (dipilih karena struktur data awalnya berupa list of edges/jalur langsung, sehingga sangat efisien saat diurutkan).
 
# 2. Edge mana saja yang dipilih?
#     - Jaringan dari GedungC ke GedungD (biaya: 1)
#     - Jaringan dari GedungA ke GedungC (biaya: 2)
#     - Jaringan dari GedungB ke GedungD (biaya: 3)

# 3. Berapa total biaya minimum?
#    - Total biaya minimum = 6 (hasil dari 1 + 2 + 3).
 
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    - Karena tujuan kasus ini adalah menghubungkan seluruh gedung agar saling 
#      terkoneksi satu sama lain tanpa redundansi (tanpa membuang kabel untuk 
#      membuat rute ganda/siklus), dengan pengeluaran total biaya yang paling minimal.