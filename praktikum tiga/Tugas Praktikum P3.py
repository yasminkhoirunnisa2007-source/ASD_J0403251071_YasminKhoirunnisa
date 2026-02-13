# ===============================
# Class Node
# ===============================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# ===============================
# Class Doubly Linked List
# ===============================
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # untuk menambahkan node di akhir
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

    # untuk menghapus node berdasarkan nilai tertentu
    def delete_node(self, key):
        curr = self.head

        # untuk cari node
        while curr and curr.data != key:
            curr = curr.next

        # Jika data tidak ditemukan
        if curr is None:
            print(f"Node dengan data {key} tidak ditemukan.")
            return

        # Jika node adalah head
        if curr == self.head:
            self.head = curr.next
            if self.head:
                self.head.prev = None
        else:
            if curr.next:
                curr.next.prev = curr.prev
            if curr.prev:
                curr.prev.next = curr.next

        curr = None

    # untuk menampilkan isi list
    def display(self):
        curr = self.head
        elements = []

        while curr:
            elements.append(str(curr.data))
            curr = curr.next

        print(" <-> ".join(elements) if elements else "list kosong")


# ===============================
# Program Utama (Testing)
# ===============================
DLL = DoublyLinkedList()

DLL.append(10)
DLL.append(20)
DLL.append(30)

print("Sebelum dihapus:")
DLL.display()

DLL.delete_node(20)
print("Setelah dihapus 20:")
DLL.display()
