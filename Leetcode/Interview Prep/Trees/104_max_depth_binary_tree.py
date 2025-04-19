from tree_utils import create_tree, print_tree

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        stack = [[root, 1]]
        counter = 0
        while stack:
            node, depth = stack.pop()
            if node:
                counter = max(counter, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return counter

tree = [3,9,20,None,None,15,7]
root = create_tree(tree)
print(f"Given tree: {tree}")
s = Solution()
print(s.maxDepth(root))