class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[-1], nums[-2])
        best = [0]*len(nums)
        best[0], best[1], best[2] = nums[0], nums[1], nums[0]+nums[2]
        for h in range(3, len(nums)):
            best[h] = max(best[h-3]+nums[h], best[h-2]+nums[h])
        return max(best[-1], best[-2])
