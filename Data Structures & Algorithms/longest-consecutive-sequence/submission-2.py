class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        i = 0
        seq = 0
        while numset and i < len(nums):
            if nums[i]-1 not in numset and nums[i] in numset:
                temp = 1
                numset.remove(nums[i])
                while nums[i]+temp in numset:
                    numset.remove(nums[i]+temp)
                    temp += 1
                seq = max(temp, seq)
            i += 1
        return seq

        
