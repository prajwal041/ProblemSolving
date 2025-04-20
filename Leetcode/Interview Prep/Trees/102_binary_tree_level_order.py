from Leetcode.rev_char_word import result
from tree_utils import create_tree, print_tree
import time
def get_runtime(message):
    def get_run(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            stop = time.time()
            runtime = stop - start
            print(f"{message}: Total runtime of {func.__name__} is {runtime}")
            return result
        return wrapper
    return get_run

class Solution:
    @get_runtime("INFO")
    def levelOrder(self, root):
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return res

tree = [3,9,20,None,None,15,7]
root = create_tree(tree)
s = Solution()
print(f"Binary Tree level order Traversal: {s.levelOrder(root)}")