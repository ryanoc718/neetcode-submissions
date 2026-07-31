class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target
        if len(nums) == 0:
            return False
        l, r = 0, len(nums)-1
        mid = (r+l)//2
        if nums[mid] == target:
            return True
        if nums[mid] > target and nums[l] <= target:
            return self.search(nums[l:mid], target)
        if nums[mid] < target and nums[r] >= target:
            return self.search(nums[mid+1:r+1], target)
        return self.search(nums[l:mid], target) or self.search(nums[mid+1:r+1], target)

