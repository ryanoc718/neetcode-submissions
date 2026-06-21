class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, t):
            if (i, t) in memo:
                return memo[(i, t)]
            if i == len(nums):
                return 1 if t == target else 0
            memo[(i, t)] = dfs(i+1, t-nums[i]) + dfs(i+1, t+nums[i])
            return memo[(i, t)]
        return dfs(0, 0)