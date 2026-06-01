"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        seen = {}
        def dfs(node):
            clone = Node(node.val)
            seen[node.val] = clone
            for nei in node.neighbors:
                if nei.val in seen:
                    n = seen[nei.val]
                else:
                    n = dfs(nei)
                clone.neighbors.append(n)
            return clone
        return dfs(node)



