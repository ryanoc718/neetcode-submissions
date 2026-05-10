class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for c in range(len(s)):
            l, r = c, c
            cur = ""
            while l > -1 and r < len(s): # odd
                if s[l] != s[r]:
                    break
                cur = s[l:r+1]
                if len(cur) > len(longest):
                    longest = cur
                l -= 1
                r += 1
            l, r = c, c+1
            cur = ""
            while l > -1 and r < len(s): # even
                if s[l] != s[r]:
                    break
                cur = s[l:r+1]
                if len(cur) > len(longest):
                    longest = cur
                l -= 1
                r += 1
        return longest
                
