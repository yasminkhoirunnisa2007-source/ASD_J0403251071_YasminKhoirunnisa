#==========================================================
#Nama   : Yasmin Khoirun Nisa
#NIM    : J0403251071
#Kelas  : TPL A/P2
#==========================================================

#==========================================================
#Implementasi Dasar : Node pada Linked List
#==========================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def _init_(self, data):
        self.data = data #menyimpan nilai atau data pada suatu list
        self.next = None #pointer ini menuju ke note berikutnya (awal=none)

#1)membuat node dengan instantiasi class node'
NodeA = Node("A")
NodeB = Node("B")
NodeC = Node("C")

#2) Mendifinisikan head dan menghubungkan Node : A -> B -> C -> None
head = NodeA
NodeA.next = NodeB
NodeB.next = NodeC

#4)  Traversal: Menelusuri node dari haead sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

