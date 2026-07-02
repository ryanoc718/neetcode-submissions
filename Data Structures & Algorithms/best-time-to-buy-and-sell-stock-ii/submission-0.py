class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}      
        def dfs(i, buying):
            if i == len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            doNothing = dfs(i+1, buying)
            if buying:
                res = max(doNothing, dfs(i+1, False) - prices[i])
            else:
                res = max(doNothing, dfs(i+1, True) + prices[i])
            memo[(i, buying)] = res
            return res
        return dfs(0, True) 
            
