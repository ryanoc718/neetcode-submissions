class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = []
        for n in nums:
            if n in vals:
                return True
            vals.append(n)
        return False