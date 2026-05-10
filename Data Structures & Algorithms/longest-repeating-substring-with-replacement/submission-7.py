class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        primaryIdx = 0
        l, r = 0, 0
        counts = [0]*26
        while l < len(s) and r < len(s):
            charIdx = ord(s[r])-ord('A')
            counts[charIdx] += 1
            if counts[charIdx] > counts[primaryIdx]:
                primaryIdx = charIdx

            subs = 0
            for c in range(len(counts)):
                if c != primaryIdx:
                    subs += counts[c]
                if subs > k:
                    break
            if subs > k:
                counts[ord(s[l])-ord('A')] -= 1
                l += 1
            r += 1
        return r-l