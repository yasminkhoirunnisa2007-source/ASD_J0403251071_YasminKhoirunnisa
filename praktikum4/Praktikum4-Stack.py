#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

#==========================================================
#Implementasi Dasar : Stack
#==========================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil/instalasi
    def __init__(self, data):
        self.data = data # Menyimpan data pada list
        self.next = None # Pointer ke node berikutnya (awal=node)

#Stack ada operasi push(memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
  
    def push(self,data): #memasukkan data baru ke stack
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

        #2 node baru menunjuk ke top (node baru menjadi head)
        nodeBaru.next = self.top

        #3 geser top ke node baru
        self.top = nodeBaru

    def is_empty(self):
            return self.top is None #stack kosong jika top tidak menunjuk ke node manapun

    def pop(self): #mengambil / menghapus node paling atas
        
        if self.top is None: #jika stack kosong
            print("Stack kosong, tidak bisa melakukan pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variable (peek)
        self.top = self.top.next #geser top ke node berikutnya (node setelah top menjadi top baru)
        return data_terhapus #kembalikan data yang dihapus

    def peek(self):
        #melihat data pada top tanpa menghapusnya
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        current = self.top
        print ("Top ->", end=" ")
        while current is not None:
            print(current.data) # Menampilkan data pada node saat ini
            current = current.next # Pindah ke node berikutnya
        print("None")


#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
s.pop()
s.tampilkan()
print("Peek (Lihat Top):", s.peek())