"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        copy = {}
        oq = deque([node])
        while oq:
            n = oq.popleft()
            if n in copy:
                continue
            copy[n] = Node(n.val)
            for i in n.neighbors:
                oq.append(i)
        
        oq = deque([node])
        seen = set()
        while oq:
            n = oq.popleft()
            if n in seen:
                continue
            seen.add(n)
            for i in n.neighbors:
                oq.append(i)
                copy[n].neighbors.append(copy[i])

        return copy[node]