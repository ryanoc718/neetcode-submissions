class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        l, r = 0, 0
        longest = 0
        seen = set()
        seen.add(s[r])
        while r < len(s):
            longest = max((r-l)+1, longest)
            r += 1
            if r == len(s): break
            if s[r] in seen:
                while l < r:
                    seen.remove(s[l])
                    l += 1
                    if s[l-1] == s[r]:
                        break
            seen.add(s[r])

        return longest