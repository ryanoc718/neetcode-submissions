class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(rem, count):
            if (rem, count) in memo:
                return memo[(rem, count)]
            if rem == 0:
                return count
            if rem < 0:
                return float("inf")
            res = float("inf")
            for c in coins:
                res = min(dfs(rem-c, count+1), res)
            memo[(rem, count)] = res
            return res
        res = dfs(amount, 0) 
        return res if res != float("inf") else -1

