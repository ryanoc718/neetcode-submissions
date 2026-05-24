class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        far = 0
        for i in range(len(nums)):
            for j in range(far+1, i+nums[i]+1):
                if j < len(nums):
                    dp[j] = dp[i]+1
                if j == len(nums)-1:
                    return dp[-1]
                far = j
        return dp[-1]

        