class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        memo = {}
        def dfs(i, a):
            if (i, a) in memo:
                return memo[(i,a)]
            if a == 0:
                return True
            if a < 0 or i == len(nums):
                return False
            memo[(i, a)] = dfs(i+1, a) or dfs(i+1, a-nums[i])
            return memo[(i, a)]
        return dfs(0, sum(nums)/2)