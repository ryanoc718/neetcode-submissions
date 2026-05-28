class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        while cur not in seen:
            if cur == 1:
                return True
            seen.add(cur)
            total = 0
            for d in str(cur):
                total += int(d)**2
            cur = total
        return False