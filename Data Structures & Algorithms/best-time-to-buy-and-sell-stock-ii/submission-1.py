class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices)+1)]
        for i in range(len(prices)-1, -1, -1):
            for b in range(2):
                dp[i][b] = dp[i+1][b]
                if b:
                    dp[i][b] = max(dp[i][b], dp[i+1][0]-prices[i])
                else:
                    dp[i][b] = max(dp[i][b], dp[i+1][1]+prices[i])
        return dp[0][1]
            
