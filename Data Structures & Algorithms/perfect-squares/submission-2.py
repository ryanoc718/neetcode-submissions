class Solution:
    def numSquares(self, n: int) -> int:
        sqrs = []
        i = 1
        while i**2 <= n:
            sqrs.append(i**2)
            i += 1
        dp = [[0]*(n+1) for _ in range(len(sqrs)+1)]
        for c in range(len(dp[-1])):
            dp[-1][c] = float("inf")
        for i in range(len(sqrs)-1, -1, -1):
            for t in range(1, n+1):
                include = float("inf") if t-sqrs[i] < 0 else 1+dp[i][t-sqrs[i]]
                dp[i][t] = min(include, dp[i+1][t])
        return dp[0][n]

