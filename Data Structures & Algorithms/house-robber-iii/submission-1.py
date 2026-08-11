# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node, take):
            if not node:
                return 0
            if (node, take) in memo:
                return memo[(node, take)]
            skip = dfs(node.right, True) + dfs(node.left, True)
            if take:
                memo[(node, take)] = max(dfs(node.right, False) + dfs(node.left, False) + node.val,
                            skip)
            else:
                memo[(node, take)] = skip
            return memo[(node, take)]
        return dfs(root, True)