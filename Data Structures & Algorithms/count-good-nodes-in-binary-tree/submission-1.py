# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = 1 # for the root
        def dfs(node, m):
            if not node: return 0
            res = 0
            if node.val >= m:
                res = 1
            left = 0 if not node.left else dfs(node.left, max(node.val, m))
            right = 0 if not node.right else dfs(node.right, max(node.val, m))
            return (res + left + right)

        rootLeft = 0 if not root.left else dfs(root.left, root.val)
        rootRight = 0 if not root.right else dfs(root.right, root.val)
        res += (rootLeft + rootRight)
        return res

                