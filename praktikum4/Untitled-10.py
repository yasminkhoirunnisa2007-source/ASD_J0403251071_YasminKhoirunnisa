#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL P/A2
#==========================================================

#==========================================================
#Implementasi Dasar : Stack
#==========================================================
class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def _init_(self, data):
        self.data = data #menyimpan nilai atau data pada suatu list
        self.next = None #pointer ini menuju ke note berikutnya (awal=none)

#Stack ada operasi push(memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)

    def push(self,data): #memasukkan data baru pada stack
        #1 membuat node baru
        NodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

        #2 node baru menunjuk ke top yang lama (head lama)
        NodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = NodeBaru

    def is_empty(self):
        return self.top is None #stack kosong jika top = None
        # B -> A -> None
    def pop(self): #mengambil / menghapus node paling atas (Top/Head)

        if self.is_empty():
            print("Stack Kosong, tidak bisa pop")
            return None
        
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        # B -> A -> None
        self.top = self.top.next
        return data_terhapus
        # A -> None

    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data


    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top" , end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Node")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top)", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top)", s.peek())