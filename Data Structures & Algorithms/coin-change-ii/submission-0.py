class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)-1, -1, -1):
            for j in range(amount, -1, -1):
                if j == amount:
                    dp[i][j] = 1
                elif j+coins[i] <= amount:
                    dp[i][j] = dp[i+1][j] + dp[i][j+coins[i]]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]