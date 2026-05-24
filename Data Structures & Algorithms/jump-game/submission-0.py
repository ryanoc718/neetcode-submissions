class Solution:
    def canJump(self, nums: List[int]) -> bool:
        hops = 0
        for n in range(len(nums)-1):
            hops -= 1
            hops = max(hops, nums[n])
            if hops < 1 and nums[n] == 0:
                return False
        return True