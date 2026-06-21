class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(prices)+2)]
        for i in range(len(prices)-1, -1, -1):
            for buying in range(2):
                cooldown = dp[i+1][buying]
                if buying:
                    dp[i][buying] = max(dp[i+1][0]-prices[i], cooldown)
                else:
                    dp[i][buying] = max(dp[i+2][1]+prices[i], cooldown)
        return dp[0][1]