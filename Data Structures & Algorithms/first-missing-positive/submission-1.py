class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        largest = max(nums)
        pos = set()
        for n in nums:
            if n > 0:
                pos.add(n)
        for n in range(1, largest):
            if n not in pos:
                return n
        return max(largest+1, 1)