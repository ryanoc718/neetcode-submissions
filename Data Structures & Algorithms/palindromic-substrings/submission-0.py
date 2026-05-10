class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for c in range(len(s)):
            l, r = c, c
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                total += 1
                l -= 1
                r += 1
            l, r = c, c+1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                total += 1
                l -= 1
                r += 1
        return total