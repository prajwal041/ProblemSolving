class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBalanced(node):
    if node is not None:
        if node.left < node.data and node.right > node.data:
            print('Balanced')

'''
          3
        2   4      
'''

root = Node(3)
root.left=Node(2)
root.right=Node(4)
isBalanced(root)
