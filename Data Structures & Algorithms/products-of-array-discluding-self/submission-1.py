class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        prods = []

        for l in range(1, len(nums)):
            left[l] = left[l-1]*nums[l-1]
        for r in range(len(nums)-2, -1, -1):
            right[r] = right[r+1]*nums[r+1]
        
        for p in range(0, len(nums)):
            prods.append(left[p]*right[p])
        return prods