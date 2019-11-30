class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# class BinarySearchTree:
#     def __init__(self, root = None):
#         self.root = root
#
#     def get_root(self):
#         return self.root
#
#     def insert_helper(self, node, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             if node.data > data:
#                 if node.left is None:
#                     node.left = Node(data)
#                 else:
#                     self.insert_helper(node.left, data)
#             else:
#                 if node.right is None:
#                     node.right = Node(data)
#                 else:
#                     self.insert_helper(node.right, data)
#
#     def inorder_successor(self, node):
#         val = node
#         while val.left is not None:
#             val = val.left
#         return val
#
#     def inorder_predeccesor(self, node):
#         val = node
#         while val.right is not None:
#             val = val.right
#         return val
#
#     def delete(self, node, key):
#         if node is None:
#             return "Tree is empty"
#         if node.data>key:
#             node.left = self.delete(node.left, key)
#         elif node.data < key:
#             node.right = self.delete(node.right, key)
#         else:
#             # case 1: 1 children
#             if node.left is None:
#                 t = node.right
#                 node = None
#                 return t
#             elif node.right is None:
#                 t = node.left
#                 node = None
#                 return t
#             # case 2 : 2 children
#             t = self.inorder_successor(node.right)
#             node.data = t.data
#             node.right = self.delete(node.right, t.data)
#             return node
#
#     def search(self, node, key):
#         if node is None:
#             print("Key not found")
#             return False
#         elif node.data == key:
#             print(" key found")
#             return True
#         elif node.left < key:
#             self.search(node.right, key)
#         else:
#             self.search(node.left, key)

def insert(root, node):
    if root is None:
        root = Node(node)
    else:
        if root.data > node:
            if root.left is None:
                root.left = Node(node)
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = Node(node)
            else:
                insert(root.right, node)

def inorder_predecessor(root):
    val = root
    if val.right is not None:
        val = val.right
    return val

def inorder_successor(root):
    val = root
    if val.left is not None:
        val = val.left
    return val

def delete(root, key):
    if root is None:
        print("Empty tree")
        return
    elif root.data < key:
        root.right = delete(root.right, key)
    elif root.data > key:
        root.left = delete(root.left, key)
    else:
        if root.left is None:
            t = root.right
            root = None
            return t
        elif root.right is None:
            t = root.left
            root = None
            return t
        t = inorder_successor(root.right)
        root.data = t.data
        root.right = delete(root.right, t.data)
    return root

def search(root, key):
    if root is None:
        print("Empty tree")
        return
    elif root.data == key:
        print("Key Found")
    else:
        if root.data < key:
            search(root.right, key)
        else:
            search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

n = Node(2)
insert(n, 1)
insert(n, 3)
insert(n, 4)
insert(n, 7)
insert(n, 5)
insert(n, 6)
print("Inorder traversal")
inorder(n)
delete(n, 5)
print("-------")
inorder(n)
search(n, 2)