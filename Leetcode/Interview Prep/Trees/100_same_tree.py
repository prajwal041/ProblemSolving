from tree_utils import create_tree, print_tree

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        if p and not q:
            return False
        if not p and q:
            return False
        p_left = self.height(p.left)
        q_left = self.height(q.left)
        p_right = self.height(p.right)
        q_right = self.height(q.right)
        if p_left != q_left and p_right != q_right:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

p = [1,2,1]
q = [1,1,2]
p_tree = create_tree(p)
q_tree = create_tree(q)
print(f"p tree: {p}, q tree: {q}")
s = Solution()
print(f"Is same Tree: {s.isSameTree(p_tree, q_tree)}")