class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0, 0]
        nextdp = [0, 0]
        for i in range(len(prices)-1, -1, -1):
            for b in range(2):
                nextdp[b] = dp[b]
                if b:
                    nextdp[b] = max(nextdp[b], dp[0]-prices[i])
                else:
                    nextdp[b] = max(nextdp[b], dp[1]+prices[i])
            dp, nextdp = nextdp, dp
        return dp[1]
            
