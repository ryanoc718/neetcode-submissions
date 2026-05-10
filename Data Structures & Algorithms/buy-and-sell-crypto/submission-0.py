class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for p in prices:
            low = min(low, p)
            if p > low:
                profit = max(p-low, profit)
        return profit