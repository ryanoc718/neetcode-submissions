class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for a, b in edges:
            adj[a] = adj.get(a, []) + [b]
            adj[b] = adj.get(b, []) + [a]
        components = 0
        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            if node not in adj:
                return
            for nei in adj[node]:
                dfs(nei)
        for a, b in edges:
            if a not in seen:
                components += 1
                dfs(a)

        return components + (n-len(seen)) 
