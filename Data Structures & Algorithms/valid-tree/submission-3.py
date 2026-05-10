class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        e = {i:[] for i in range(n)}
        for s, d in edges:
            if s == d:
                return False
            e[s].append(d)
            e[d].append(s)
        if n < 2: return True
        visited, seen = set(), set()
        def dfs(v, prev):
            if v == prev or e[v] == []:
                return True
            if prev in e[v]:
                e[v].remove(prev)
            if v in visited:
                return False
            visited.add(v)
            seen.add(v)
            for c in e[v]:
                if not dfs(c, v):
                    return False
            e[v] = []
            visited.remove(v)
            return True
        if not dfs(0, -1): return False
        return len(seen) == n

                