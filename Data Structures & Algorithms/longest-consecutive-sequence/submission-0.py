class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            if n-1 not in numset:
                streak = 1
                curr = n+1
                while curr in numset:
                    streak += 1
                    curr += 1
                if streak > longest:
                    longest = streak
        return longest