class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u] += [v]
            adj[v] += [u]
        def bfs(node):
            q = deque([node])
            while q:
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for nei in adj[node]:
                    q.append(nei)
        graphs = 0
        for i in range(n):
            if i not in visited:
                graphs += 1
                bfs(i)
        return graphs
        