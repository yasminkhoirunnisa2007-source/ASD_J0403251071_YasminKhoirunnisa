class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

# untuk menambah elemen ke akhir
    def append(self, data): 
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

# untuk menampilkan isi list
    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(", ".join(elements))
 
# untuk mencari isi list
    def search(self, key):
        curr = self.head
        position = 1

        while curr:
            if curr.data == key:
                print(f"Elemen {key} ditemukan pada posisi ke-{position} dalam Doubly Linked List.")
                return
            curr = curr.next
            position += 1

        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")


# ===============================
# Program Utama
# ===============================
DLL = DoublyLinkedList()

# untuk meng- input elemen
data_list = [2, 6, 9, 14, 20]
for data in data_list:
    DLL.append(data)

print("Masukkan elemen ke dalam Doubly Linked List:")
DLL.display()

# menginput untuk mencari elemen
cari = int(input("Masukkan elemen yang ingin dicari: "))
DLL.search(cari)
