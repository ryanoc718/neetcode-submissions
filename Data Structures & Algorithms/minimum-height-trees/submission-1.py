class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for u, v in edges:
            adj[u] = [v] + adj.get(u, [])
            adj[v] = [u] + adj.get(v, [])
        def bfs(node):
            seen = set()
            q = deque([node])
            level = -1
            while q:
                level += 1
                for _ in range(len(q)):
                    node = q.popleft()
                    seen.add(node)
                    for nei in adj.get(node, []):
                        if nei not in seen:
                            q.append(nei)
            return level
        res = []
        for i in range(n):
            h = bfs(i)
            if not res or h < res[0][1]:
                res = []
                res.append([i, h])
            elif h == res[0][1]:
                res.append([i, h])
        return [i for i, h in res]

