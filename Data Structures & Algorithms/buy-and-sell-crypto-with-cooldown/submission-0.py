class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            coolDown = dfs(i+1, buying)
            if buying:
                memo[(i, buying)] =  max(dfs(i+1, False) - prices[i], coolDown)
            if not buying:
                memo[(i, buying)] = max(dfs(i+2, True) + prices[i], coolDown)
            return memo[(i, buying)]
        return dfs(0, True)