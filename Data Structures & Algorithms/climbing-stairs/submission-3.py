class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        res = 0
        one, two = 1, 0
        while count < n:
            res = one+two
            two = one
            one = res
            count += 1
        return res