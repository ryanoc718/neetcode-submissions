class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        count = 2
        res = 0
        one, two = 2, 1
        while count < n:
            res = one+two
            two = one
            one = res
            count += 1
        return res