# Identitas
print("Nama : Yasmin Khoirun Nisa")
print("NIM  : J0403251071")

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            # jika sama, diabaikan (tidak dimasukkan)
        else:
            self.data = data

# Fungsi Traversal
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)

def preorder(root, result):
    if root:
        result.append(root.data)
        preorder(root.left, result)
        preorder(root.right, result)

def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.data)

# Persiapan Data
nim_last_two = 71
root = Node(nim_last_two)

# HAPUS root dari list agar tidak dobel
data_list = [nim_last_two + 20, nim_last_two + 30,
             nim_last_two + 10, nim_last_two + 30,
             nim_last_two + 15]

# Membangun Tree
for val in data_list:
    root.insert(val)

# Traversal
in_res, pre_res, post_res = [], [], []
inorder(root, in_res)
preorder(root, pre_res)
postorder(root, post_res)

# Output
print("In-order Traversal  :", in_res)
print("Pre-order Traversal :", pre_res)
print("Post-order Traversal:", post_res)
