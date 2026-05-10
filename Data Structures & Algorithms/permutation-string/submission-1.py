class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        r, l = 0, len(s1)-1
        count1 = {}
        count2 = {}
        for c in s1:
            count1[c] = count1.get(c, 0)+1
        for c in s2[r:l+1]:
            count2[c] = count2.get(c, 0)+1
        while l < len(s2)-1:
            if count1 == count2:
                return True
            l += 1
            count2[s2[l]] = count2.get(s2[l], 0)+1
            count2[s2[r]] -= 1
            if count2[s2[r]] == 0:
                count2.pop(s2[r])
            r += 1
        return count1 == count2