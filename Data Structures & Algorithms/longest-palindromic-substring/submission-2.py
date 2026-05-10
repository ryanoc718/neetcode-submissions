class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for c in range(len(s)):
            l, r = c, c
            while l >= 0 and r <= len(s)-1:
                if s[l] != s[r]:
                    break
                if (r-l)+1 > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
            l, r = c, c+1
            while l >= 0 and r <= len(s)-1:
                if s[l] != s[r]:
                    break
                if (r-l)+1 > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
        return longest
            