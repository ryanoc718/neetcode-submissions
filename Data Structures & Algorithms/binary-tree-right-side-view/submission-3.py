# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        dq = deque([root])
        while dq:
            res.append(dq[0].val)
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.right: dq.append(node.right)
                if node.left: dq.append(node.left)
        return res