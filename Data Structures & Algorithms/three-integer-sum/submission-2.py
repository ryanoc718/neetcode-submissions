class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = 0
        res = []
        while n < len(nums):
            if nums[n] > 0:
                break
            l, r = n+1, len(nums)-1
            while l < r:
                s = nums[n] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[n], nums[l], nums[r]])
                    while r > l+1 and nums[r] == nums[r-1]:
                        r -= 1 
                    r -= 1
                elif s < 0:
                    while l < r-1 and nums[l] == nums[l+1]:
                        l += 1   
                    l += 1
                else:
                    while r > l+1 and nums[r] == nums[r-1]:
                        r -= 1   
                    r -= 1

            while n < len(nums)-1 and nums[n] == nums[n+1]:
                n += 1        
            n += 1
        return res


