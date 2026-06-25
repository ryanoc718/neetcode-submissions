class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        def isPal(w):
            l, r = 0, len(w)-1
            while l < r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPal(s[:l]+s[l+1:]) or isPal(s[:r]+s[r+1:])

        return True