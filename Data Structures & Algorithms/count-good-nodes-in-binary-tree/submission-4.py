# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(pathMax, node):
            if not node: return 0
            if node.val >= pathMax:
                pathMax = node.val
                return 1 + dfs(pathMax, node.right)+dfs(pathMax, node.left)
            return dfs(pathMax, node.right)+dfs(pathMax, node.left)
        return dfs(root.val, root)