# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        dq = deque([[root, -101]])
        while dq:
            for i in range(len(dq)):
                node, m = dq.popleft()
                if node.val >= m:
                    res += 1
                    m = node.val
                if node.left: dq.append([node.left, m])
                if node.right: dq.append([node.right, m])
        return res
                