class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        for word in strs:
            grouped = False
            for group in groups:
                if self.isAnagram(word, group[0]):
                    group.append(word)
                    grouped = True
            if not grouped:
                groups.append([word])
        return groups

    def isAnagram(self, s:str , r:str) -> bool:
        if len(s) != len(r):
            return False
        
        mapS = {}
        mapR = {}
        for i in range(0, len(s)):
            if s[i] in mapS:
                mapS[s[i]] += 1
            else:
                mapS[s[i]] = 1
            if r[i] in mapR:
                mapR[r[i]] += 1
            else:
                mapR[r[i]] = 1
        return mapS == mapR