# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, prevLeft, prevRight, parent, isLeft):
            if not node: return True
            val = node.val
            if isLeft:
                if val >= parent: return False
                if val <= prevRight: return False
                prevLeft = parent
            else:
                if val <= parent: return False
                if val >= prevLeft: return False
                prevRight = parent
            return (valid(node.left, prevLeft, prevRight, val, True) and
                    valid(node.right, prevLeft, prevRight, val, False))

        return (valid(root.left, 1001, -1001, root.val,True) and
                    valid(root.right, 1001, -1001, root.val,False)) 
