class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first = True
        i = 0
        res = ""
        while i < len(word1) and i < len(word2):
            if first:
                first = False
                res += word1[i]
            else:
                first = True
                res += word2[i]
                i += 1
        res += word1[i:]
        res += word2[i:]
        return res
