class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[-1], nums[-2])
        nums[2] += nums[0]
        for h in range(3, len(nums)):
            nums[h] += max(nums[h-3], nums[h-2])
        return max(nums[-1], nums[-2])
