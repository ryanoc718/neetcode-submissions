class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        for i in range(0, len(nums)):
            cur = nums[i]
            res = max(cur, res)
            for j in range(i+1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)
        return res
            