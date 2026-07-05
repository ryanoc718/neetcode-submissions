class Solution:
    def numSquares(self, n: int) -> int:
        sqrs = []
        i = 1
        while i**2 <= n:
            sqrs.append(i**2)
            i += 1

        memo = {}
        def dfs(i, t):
            if (i, t) in memo:
                return memo[(i, t)]
            if i < 0 or t > n:
                return float("inf")
            if t == n:
                return 0
            memo[(i, t)] = min(1+dfs(i, t+sqrs[i]), dfs(i-1, t))
            return memo[(i, t)]
        return dfs(len(sqrs)-1, 0)

