class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combo = []
        def dfs(i):
            if len(combo) == k:
                res.append(combo.copy())
                return
            if i > n:
                return
            combo.append(i)
            dfs(i+1)
            combo.pop()
            dfs(i+1)
        dfs(1)
        return res