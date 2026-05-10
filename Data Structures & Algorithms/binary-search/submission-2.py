class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, mid = 0, len(nums)-1, len(nums)//2
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while l < r and l < mid:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid
            mid = (r+l)//2
        return mid if nums[mid] == target else -1