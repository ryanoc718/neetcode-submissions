class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        windows = []
        l = 0
        for r in range(k-1, len(nums)):
            windows.append(sorted(nums[l:r+1]))
            l += 1
        for w in windows:
            res.append(w[-1])
        return res
        
