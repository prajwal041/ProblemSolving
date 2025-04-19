from tree_utils import create_tree, print_tree

class Solution:
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))

tree = [2,1,3]
root = create_tree(tree)
print(f"Given tree: {tree}")
s = Solution()
print(f"Is valid Binary search Tree: {s.isValidBST(root)}")