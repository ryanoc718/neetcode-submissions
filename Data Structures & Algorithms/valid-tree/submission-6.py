class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for x, y in edges:
            adj[x] = [y] + adj.get(x, [])
            adj[y] = [x] + adj.get(y, [])
        seen = set()
        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)
            for nei in adj.get(node, []):
                if nei != prev and not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(seen) == n