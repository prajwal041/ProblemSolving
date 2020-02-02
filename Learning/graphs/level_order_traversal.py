class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        lh = height(node.left)
        rh = height(node.right)

        if lh > rh :
            return lh+1
        else:
            return rh+1

def printLevel(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenOrder(root, i)

def printGivenOrder(root, level):
    if root is None:
        return
    if level ==1:
        print(root.data, end=", ")
    elif level>1:
        printGivenOrder(root.left, level-1)
        printGivenOrder(root.right, level-1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal\n")
printLevel(root)
