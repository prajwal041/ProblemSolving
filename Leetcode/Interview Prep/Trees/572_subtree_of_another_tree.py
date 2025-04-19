from tree_utils import create_tree, print_tree

class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        return False

root = [3,4,5,1,2]
subRoot = [4,1,2]
tree, subTree = create_tree(root), create_tree(subRoot)
print(f"given tree: {root}, subTree: {subRoot}")
s = Solution()
print(f"Is Subtree: {s.isSubtree(tree, subTree)}")
