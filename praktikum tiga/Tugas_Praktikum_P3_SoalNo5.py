# ===============================
# Class Node (Single Linked List)
# ===============================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ===============================
# Class Single Linked List
# ===============================
class SingleLinkedList:
    def __init__(self):
        self.head = None

    # untuk menambah node di akhir
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    # untuk menampilkan isi list
    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "list kosong")

    # ===============================
    # Method reverse (tanpa list baru)
    # ===============================
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next   # simpan next
            curr.next = prev        # balik arah pointer
            prev = curr             # geser prev
            curr = next_node        # geser curr

        self.head = prev

SLL = SingleLinkedList()

SLL.append(10)
SLL.append(20)
SLL.append(30)
SLL.append(40)

print("Sebelum dibalik:")
SLL.display()

SLL.reverse()

print("Setelah dibalik:")
SLL.display()
