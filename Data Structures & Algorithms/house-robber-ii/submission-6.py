class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        rob1, rob2 = 0, 0
        for num in nums[:-1]:
            temp = max(rob2+num, rob1)
            rob2 = rob1
            rob1 = temp
        res = rob1
        rob1, rob2 = 0, 0
        for i in range(len(nums)-1, 0, -1):
            temp = max(rob2+nums[i], rob1)
            rob2 = rob1
            rob1 = temp
        return max(res, rob1)
