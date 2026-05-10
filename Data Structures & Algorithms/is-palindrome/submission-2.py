class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "123567890"
        clean = ""
        for c in s:
            if c in alpha:
                clean += chr((ord(c)-ord('A'))+ord('a'))
            elif ord(c)-ord('a') > -1 and ord(c)-ord('a') < 26:
                clean += c
            elif c in nums:
                clean += c
        l, r = 0, len(clean)-1
        while l < r:
            if clean[l] != clean[r]:
                return False
            else:
                l += 1
                r -= 1
        return True