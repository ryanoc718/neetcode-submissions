class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for v in range(1, len(prices)):
            lowest = min(prices[v], lowest)
            profit = max(prices[v]-lowest, profit)
        return profit