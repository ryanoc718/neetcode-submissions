class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for c in range(len(s)):
            l, r = c, c
            while l > -1 and r < len(s) and s[l] == s[r]:
                if 1+(r-l) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
            l, r = c, c+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if 1+(r-l) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
        return longest
            
