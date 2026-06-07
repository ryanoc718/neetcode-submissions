class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for x, y in edges:
            adj[x] = [y] + adj.get(x, [])
            adj[y] = [x] + adj.get(y, [])
        found = set()
        q = deque([(0, -1)])
        while q:
            node, prev = q.popleft()
            if node in found:
                return False
            found.add(node)
            for nei in adj.get(node, []):
                if nei != prev:
                    q.append((nei, node))
        return len(found) == n
            
