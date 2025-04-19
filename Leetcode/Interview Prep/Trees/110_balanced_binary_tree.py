from tree_utils import create_tree, print_tree

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

tree = [1,2,2,3,3,None,None,4,4]
root = create_tree(tree)
print(f"Given Tree: {tree}")
s = Solution()
print(f"IsBalanced tree: {s.isBalanced(root)}")