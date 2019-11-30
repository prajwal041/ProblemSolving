class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:

    def insert(self, root, key):
        if root is None:
            root = Node(key)
        elif root.data <key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)
        if balance > 1 and key < root.left.data:
            return self.rotateRight(root)
        if balance < -1 and key > root.right.data:
            return self.rotateLeft(root)
        if balance > 1 and key > root.left.data:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and key < root.right.data:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def height(self, root):
        if root is None:
            return 0
        return root.height

    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def rotateLeft(self, z):
        y = z.right
        x = y.left

        y.left = z
        z.right = x

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rotateRight(self, z):
        y = z.left
        x = y.right

        y.right = z
        z.left = x

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def preorder(self, root):
        if root:
            print(f"{root.data}", end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


if __name__ == "__main__":
    root = None
    t = AVL()
    root = t.insert(root, 10)
    root = t.insert(root, 20)
    root = t.insert(root, 30)
    root = t.insert(root, 40)
    root = t.insert(root, 50)
    root = t.insert(root, 25)


    print("Preorder traversal")
    """The constructed AVL Tree would be 
                30 
               /  \ 
             20   40 
            /  \     \ 
           10  25    50
    """

    t.preorder(root)