class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            mid = (l+r)//2
            if nums[r] < nums[mid]:
                l = mid+1
            else:
                r = mid-1
        
            res = min(res, nums[mid])
        
        return res