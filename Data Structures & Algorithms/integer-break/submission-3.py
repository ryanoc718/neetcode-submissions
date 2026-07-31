class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(total, prod):
            if (total, prod) in memo:
                return memo[(total, prod)]
            if total == 0:
                return prod
            if total < 0:
                return float("-inf")
            res = float("-inf")
            for i in range(1, min(total+1, n)):
                res = max(res, dfs(total-i, prod*i))
            memo[(total, prod)] = res
            return res
        return dfs(n, 1)