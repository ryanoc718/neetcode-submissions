class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        one, two, three = 1, 0, 0
        for _ in range(2, n+1):
            temp = one + two + three
            three, two, one = two, one, temp
        return one