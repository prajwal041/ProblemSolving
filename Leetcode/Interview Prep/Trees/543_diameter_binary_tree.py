from tree_utils import create_tree, print_tree

class Solution:
    def diameterOfBinaryTree(self, root):
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right)

            return 1 + max(left, right)
        dfs(root)
        return res

tree = [1,2,3,4,5]
root = create_tree(tree)
print(f"Given tree: {root}")
s = Solution()
print(f"Diameter of tree is: {s.diameterOfBinaryTree(root)}")