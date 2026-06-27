class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:     
        memo = {}
        def dfs(total):
            if total in memo:
                return memo[total]
            if total == 0:
                return 1
            if total < 0:
                return 0
            res = 0
            for n in nums:
                res += dfs(total-n)
            memo[total] = res
            return res

        return dfs(target)
            