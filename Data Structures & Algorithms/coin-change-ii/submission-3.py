class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, a):
            if (i, a) in memo:
                return memo[(i, a)]
            if a == 0:
                memo[(i, a)] = 1
                return 1
            if i == len(coins) or a < 0:
                memo[(i, a)] = 0
                return 0
            memo[(i, a)] = dfs(i+1, a) + dfs(i, a-coins[i])
            return memo[(i, a)]
        return dfs(0, amount)