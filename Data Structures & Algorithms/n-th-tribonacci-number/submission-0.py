class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n < 3:
            return 1
        one, two, three = 1, 1, 0
        for _ in range(3, n+1):
            temp = one + two + three
            three, two, one = two, one, temp
        return one