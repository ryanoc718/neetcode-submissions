class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        first, last = nums[1:].copy(), nums[:-1].copy()
        first[1] = max(first[0], first[1])
        for h in range(2, len(first)):
            first[h] = max(first[h-1], first[h-2]+first[h])
        last[1] = max(last[0], last[1])
        for h in range(2, len(last)):
            last[h] = max(last[h-1], last[h-2]+last[h])
        return max(first[-1], last[-1])
