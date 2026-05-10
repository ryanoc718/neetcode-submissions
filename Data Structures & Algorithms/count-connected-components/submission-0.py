class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphs = []
        e = {i:[] for i in range(n)}
        for i, j in edges:
            e[i].append(j)
            e[j].append(i)
        checked = set()
        visited = set()
        def dfs(v, parent):
            if v in visited:
                return
            visited.add(v)
            checked.add(v)
            for c in e[v]:
                if c == parent:
                    continue
                dfs(c, v)
            
        for i in range(n):
            if i in checked:
                continue
            visited = set()
            dfs(i, -1)
            graphs.append(list(visited))
        return len(graphs)

