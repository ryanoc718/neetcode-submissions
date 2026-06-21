class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*m
        for r in range(1, n):
            nextDp = [1]*m
            for c in range(1, m):
                nextDp[c] = dp[c] + nextDp[c-1]
            dp, nextDp = nextDp, dp
        return dp[-1]