class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u] += [v]
            adj[v] += [u]
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            
        graphs = 0
        for i in range(n):
            if i not in visited:
                graphs += 1
                dfs(i)
        return graphs
        