class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, total):
            if total == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            if (i, total) in memo:
                return memo[(i, total)]
            memo[(i,total)] = dfs(i+1, total-nums[i]) + dfs(i+1, total+nums[i])
            return memo[(i, total)]
        return dfs(0, 0)