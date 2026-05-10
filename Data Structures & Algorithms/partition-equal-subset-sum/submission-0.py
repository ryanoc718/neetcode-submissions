class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(i, total, rem):
            if total == rem:
                return True
            if total > rem:
                return False
            if i >= len(nums):
                return False
            return dfs(i+1, total+nums[i], rem-nums[i]) or dfs(i+1, total, rem)
        return dfs(0, 0, sum(nums))
        