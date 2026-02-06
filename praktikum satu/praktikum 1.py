#---------------------------------------------------------------------------
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#----------------------------------------------------------------------------------

print("---- Membuka file dalam satu satu string ----")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Tipe Data :", type(isi_file))

print("===== Membuka file per baris =====")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() # Menghilangkan karakter garis baru
        print(f"Baris ke-{jumlah_baris}")
        print(f"Isinya: {baris}")

#============================================================
# Praktikum 1 Konsep ADT dan File Handling 
# Latihan dasar 2 Parsing baris menjadi data satuan dan menampilkan dalam bentuk kolom data 
#============================================================


with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah data variabel satuan dan simpan ke 
        print("NIM  :", nim, "| Nama : ", nama, "| Nilai :", nilai) #menampilkan satuan data dalam bentuk kolom 
       

#---------------------------------------------------------------------------
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca Data dan Menyimpannya ke Struktur Data List
#---------------------------------------------------------------------------

# Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom data
data_list = [] #inisialisasi list untuk menampung data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print(f"Nim: {nim} | Nama: {nama} | Nilai: {nilai}")
        data_list.append([nim, nama, int(nilai)])

print("===== Menampilkan List =====")
print(data_list)
print("Contoh record ke-1", data_list[0])
print("Contoh record ke-1", data_list[1])
print("Jumlah record pada list", len(data_list))

#============================================================
# Praktikum 1 Konsep ADT dan File Handling 
# Latihan 4 membaca data dan menyimpannya ke dalam struktur data dictionary 
#============================================================


data_dict = {} #inisialisasi dictionary 
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah data variabel satuan dan simpan ke 
        data_dict[nim] = {
            'nama': nama,
            'nilai': int(nilai)
        } 
print("====Menampilkan Data Dictionary====")
print(data_dict)