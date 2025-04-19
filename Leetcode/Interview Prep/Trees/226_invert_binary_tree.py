from tree_utils import create_tree, print_tree

class dfs:
    def solution(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
tree = [4,2,7,1,3,6,9]
print(f"Given Tree: {tree}")
root = create_tree(tree)
dfs = dfs()
print(f"Inverted Tree: {print_tree(dfs.solution(root))}")