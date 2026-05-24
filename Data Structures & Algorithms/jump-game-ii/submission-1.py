class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1, i+nums[i]+1):
                if j < len(nums) and dp[j] == 0:
                    dp[j] = dp[i]+1
                if j == len(nums)-1:
                    return dp[-1]
        return dp[-1]

        