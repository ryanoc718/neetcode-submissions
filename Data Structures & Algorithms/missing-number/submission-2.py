class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([0+(i+1)-nums[i] for i in range(len(nums))]) 