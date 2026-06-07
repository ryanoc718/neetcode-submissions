class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for u, v in edges:
            adj[u] = [v] + adj.get(u, [])
            adj[v] = [u] + adj.get(v, [])
        leaves = True
        while leaves:
            leaves = False
            remove = []
            for node in adj:
                if len(adj[node]) < 2:
                    remove.append(node)
                    leaves = True
            for node in remove:
                connections = adj.pop(node, [])
                for c in connections:
                    if c in adj:
                        adj[c].remove(node)

        for u, v in edges[::-1]:
            if u in adj and v in adj[u]:
                return sorted([u, v])
        return edges[0]