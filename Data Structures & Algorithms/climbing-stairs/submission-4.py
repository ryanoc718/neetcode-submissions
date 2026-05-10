class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1
        total = 0
        for i in range(n):
            total = one + two
            temp = one
            one = two
            two = total
        return total