class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [0]*len(nums)
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        for h in range(2, len(nums)):
            dp[h] = max(dp[h-1],nums[h]+dp[h-2])
        return dp[-1]