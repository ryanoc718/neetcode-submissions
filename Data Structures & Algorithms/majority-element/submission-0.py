class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        cnt = 1
        for n in nums[1:]:
            if n == res:
                cnt += 1
            else:
                cnt -= 1
            if cnt <= 0:
                cnt = 0
                res = n
        return res


