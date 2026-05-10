class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         nums2 = []
         for num in nums:
            if num in nums2:
                return True
            nums2.append(num)
         return False