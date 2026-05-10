# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        ps, qs = [p], [q]
        while ps and qs:
            nodep, nodeq = ps.pop(), qs.pop()
            if not nodep.val == nodeq.val:
                return False
            if (nodep.left or nodeq.left) and not (nodep.left and nodeq.left):
                return False
            if (nodep.right or nodeq.right) and not (nodep.right and nodeq.right):
                return False
            if nodep.right:
                ps.append(nodep.right)
                qs.append(nodeq.right)
            if nodep.left:
                ps.append(nodep.left)
                qs.append(nodeq.left)
        return len(ps) == len(qs)
            

