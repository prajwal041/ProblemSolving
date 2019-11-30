'''
            4
          /   \
        2      2
      /  \    /  \
    1    3   5    7

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search_binary_tree(root, item):
    if root is None:
        return 0
    left_tree = search_binary_tree(root.left, item)
    if left_tree == item:
        print(f"Found {item}")
    # if left_tree == -1:
    #     return -1

    right_tree = search_binary_tree(root.right, item)
    if right_tree == item:
        print(f"Found {item}")
    # if right_tree == -1:
    #     return -1

    # right_tree = search_binary_tree(root.right)
    # if right_tree ==-1:
    #     return -1
    # if abs(left_tree - right_tree)>1:
    #     return -1
    return root.data


root = Node(4)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print(search_binary_tree(root, 2))

