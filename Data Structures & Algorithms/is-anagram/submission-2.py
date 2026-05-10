class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        ss, tt = [0]*26, [0]*26
        for c in range(len(s)):
            ss[ord(s[c])-ord('a')] += 1
            tt[ord(t[c])-ord('a')] += 1
        return ss == tt