class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        i, j = 0, 1
        while j < len(s):
            count = {}
            for c in s[i: j+1]:
                count[c] = count.get(c, 0)+1
            mostCommon = 'A'
            highFreq = 0
            for key in count:
                if count[key] > highFreq:
                    highFreq = count[key]
                    mostCommon = key
            windowLength = (j-i)+1
            if windowLength-highFreq <= k:
                j += 1
            else:
                i += 1
                j += 1
        return (j-i)
            
            
            
            
