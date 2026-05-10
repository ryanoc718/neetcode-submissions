class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = set()
        def dfs(i, total, rem):
            if total == rem:
                return True
            if total > rem or (i,total) in memo:
                return False
            memo.add((i,total))
            if i >= len(nums):
                return False
            return dfs(i+1, total+nums[i], rem-nums[i]) or dfs(i+1, total, rem)
        return dfs(0, 0, sum(nums))
        