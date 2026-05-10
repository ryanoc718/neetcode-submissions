class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dpr = [0]*len(nums)
        dpr[0], dpr[1] = nums[0], max(nums[0],nums[1])
        for h in range(2, len(nums)-1):
            dpr[h] = max(dpr[h-1], nums[h]+dpr[h-2])
        dpl = [0]*len(nums)
        dpl[-1], dpl[-2] = nums[-1], max(nums[-1],nums[-2])
        for h in range(len(nums)-3, 0, -1):
            dpl[h] = max(dpl[h+1], nums[h]+dpl[h+2])
        return max(dpl[1], dpr[-2])
        