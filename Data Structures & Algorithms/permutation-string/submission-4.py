class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        one, two = [0]*26, [0]*26
        for c in range(len(s1)):
            one[ord(s1[c])-ord('a')] += 1
            two[ord(s2[c])-ord('a')] += 1
        l, r = 0, len(s1)-1
        while r < len(s2):
            if one == two:
                return True
            two[ord(s2[l])-ord('a')] -= 1
            l += 1
            r += 1
            if r < len(s2):
                two[ord(s2[r])-ord('a')] += 1
        return False
            
        
        