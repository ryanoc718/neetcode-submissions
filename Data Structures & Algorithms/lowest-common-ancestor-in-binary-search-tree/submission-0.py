# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dq = deque([root])
        lowest = root
        
        def containsNodes(node):
            if not node: return False
            stack = [node]
            foundP, foundQ = [], []
            while stack:
                node = stack.pop()
                if node.val == p.val:
                    foundP = True
                if node.val == q.val:
                    foundQ = True
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                if foundP and foundQ:
                    return True

        while dq:
            node = dq.popleft()
            if containsNodes(node):
                lowest = node
            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)
        return lowest
        
        