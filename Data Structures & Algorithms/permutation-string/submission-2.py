class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l, r = 0, len(s1)-1
        a = [0]*26
        for c in range(l, r+1):
            a[ord(s1[c])-ord('a')] += 1
            a[ord(s2[c])-ord('a')] -= 1
        while r < len(s2):
            if a == [0]*26:
                return True
            a[ord(s2[l])-ord('a')] += 1
            l += 1
            r += 1
            if r < len(s2):
                a[ord(s2[r])-ord('a')] -= 1
        return a == [0]*26
        