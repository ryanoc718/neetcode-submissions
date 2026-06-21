class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[n-1][m-1]