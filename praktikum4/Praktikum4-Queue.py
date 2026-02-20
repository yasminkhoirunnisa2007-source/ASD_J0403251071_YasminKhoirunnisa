#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL P/A2
#==========================================================

#==========================================================
#Implementasi Dasar : Queue
#==========================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def _init_(self, data):
        self.data = data #menyimpan nilai atau data pada suatu list
        self.next = None #pointer ini menuju ke note berikutnya (awal=none)

class Queue:
    #membuat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    #membuat fungsi untuk menambahkan data baru pada bagian belakang
    def enqueue(self,data):
        NodeBaru = Node(data)

        #jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = NodeBaru
            self.rear = NodeBaru
            return
        #jika queue tidak kosong, maka letakakn data baru ke setelah rear
        self.rear.next = NodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = NodeBaru #Jadikan data baru sebagai rear

    def tampilkan(self):
        current = self.front
        print("Front ->", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")

#Instantiasi class queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()