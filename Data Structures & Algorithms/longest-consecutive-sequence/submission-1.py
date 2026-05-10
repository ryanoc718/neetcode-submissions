class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        for n in nums:
            seq[n] = n

        for n in nums:
            if n-1 in seq:
                seq[n] = seq[seq[n-1]]
                
        for n in nums[::]:
            if n-1 in seq:
                seq[n] = seq[seq[n-1]]
        m = 0
        for n in seq:
            m = max(m, n-seq[n]+1)
        print(seq)
        return m
