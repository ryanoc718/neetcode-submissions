# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        dq = deque([(root, root.val)])
        while dq:
            node, pathMax = dq.popleft()
            if node.val >= pathMax:
                pathMax = node.val
                res += 1
            if node.left: dq.append((node.left, pathMax))
            if node.right: dq.append((node.right, pathMax))
        return res



                