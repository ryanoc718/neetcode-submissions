class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += i+1
            total -= nums[i]
        return total 