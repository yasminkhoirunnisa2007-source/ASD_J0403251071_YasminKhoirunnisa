#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL P/A2
#==========================================================

#==========================================================
#Implementasi Dasar : Queue
#==========================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil/instalasi
    def __init__(self, data):
        self.data = data # Menyimpan data pada list
        self.next = None # Pointer ke node berikutnya (awal=node)

class Queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None #Queue kosong jika front tidak menunjuk ke node manapun

    #membuat fungsi untuk menambahkan data baru pada bagian bagian paling belakang
    def enqueue(self, data):
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        

        #jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #Letakan data baru pada bagian paling belakang
        self.rear = nodeBaru #Jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data pada bagian paling depan (front)
        data_terhapus = self.front.data #lihat data paling depan

        #geser front ke node berikutnya (node setelah front menjadi front baru)
        self.front = self.front.next

        #Jika setelah geser front menjadi None, maka queue menjadi kosong
        #rear juga harus jadi None
        if self.front is None:
            self.rear = None

        return data_terhapus #kembalikan data yang dihapus


    def tampilkan(self):
        current = self.front
        print("Front -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

#Instansiasi class Queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
print("Dequeue:", q.dequeue())
q.tampilkan()