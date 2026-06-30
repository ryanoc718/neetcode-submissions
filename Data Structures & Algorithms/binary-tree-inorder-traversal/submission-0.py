# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(n):
            if not n:
                return
            inorder(n.left)
            res.append(n.val)
            inorder(n.right)
        inorder(root)
        return res