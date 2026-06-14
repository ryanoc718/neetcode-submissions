class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        two = nums[0]
        one = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = one
            one = max(nums[i]+two, temp)
            two = temp
        return one
