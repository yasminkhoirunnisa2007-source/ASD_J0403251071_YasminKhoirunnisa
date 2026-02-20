#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

#==========================================================
#Implementasi Dasar : Node pada Linked List
#==========================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil/instalasi
    def __init__(self, data):
        self.data = data # Menyimpan data pada list
        self.next = None # Pointer ke node berikutnya (awal=node)

#1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mendefinisikan head dan Menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) # Menampilkan data pada node saat ini
    current = current.next # Pindah ke node berikutnya
