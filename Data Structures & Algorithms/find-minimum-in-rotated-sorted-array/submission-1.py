class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mid = (l+r)//2
        small = nums[0]
        while l <= r:
            small = min(small, nums[mid])
            if nums[r] < nums[mid]:
                l = mid+1
            else:
                r = mid-1
            mid = (l+r)//2
        return small