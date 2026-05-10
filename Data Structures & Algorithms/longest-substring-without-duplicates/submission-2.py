class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        while r < len(s):
            if r == len(s)-1 and len(set(s[l:])) == (r-l)+1:
                r += 1
            elif len(set(s[l:r+1])) == (r-l)+1:
                r += 1
            else:
                l+=1
                r+=1
                
        return (r-l)