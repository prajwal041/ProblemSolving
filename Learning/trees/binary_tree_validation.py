class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def is_balanced(root):
    if root is None:
        return True
    return is_balanced(root.left) and is_balanced(root.right) and abs(height(root.left) - height(root.right))<=1


"""
Improvised Solution
"""
def balanced(root):
    if root is None:
        return 0
    lh = balanced(root.left)
    if lh == -1:
        return -1

    rh = balanced(root.right)
    if rh == -1:
        return -1

    if abs(lh-rh)>1:
        return -1
    return max(lh, rh)+1

'''
        4                               
    2       6
  1    3   5   7                      
                    
                        
'''

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(7)
# root.right.right.right = Node(8)
# root.right.right.right.right = Node(9)
# root.right.right.right.right.right = Node(10)
print(is_balanced(root))
print(balanced(root))