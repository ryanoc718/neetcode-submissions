# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.val == subRoot.val and self.sameTree(node, subRoot):
                    return True
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
        return False
        
    def sameTree(self, r, s):
        if not r and not s: return True
        if not r or not s: return False
        left = self.sameTree(r.left, s.left)
        right = self.sameTree(r.right, s.right)
        return r.val == s.val and left and right











