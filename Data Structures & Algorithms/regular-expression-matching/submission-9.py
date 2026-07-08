class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s) and j == len(p):
                return True
            if j >= len(p):
                return False
            if j + 1 < len(p) and p[j+1] == "*":
                memo[(i, j)] = ((i < len(s) and (s[i] == p[j] or p[j] == ".") and (dfs(i+1, j) or dfs(i+1, j+2)))
                                 or dfs(i, j+2))
            elif i < len(s) and s[i] == p[j] or p[j] == ".":
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                return False
            return memo[(i, j)]
        return dfs(0, 0)