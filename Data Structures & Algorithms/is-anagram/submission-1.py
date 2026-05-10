class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS = {}
        mapT = {}

        for i in range(0, len(s)):
            if s[i] in mapS:
                mapS[s[i]] += 1
            else:
                mapS[s[i]] = 1
            if t[i] in mapT:
                mapT[t[i]] += 1
            else:
                mapT[t[i]] = 1

        if len(mapS) != len(mapT):
            return False
        
        for i in mapS:
            if i not in mapT or mapT[i] != mapS[i]:
                return False
        return True
            