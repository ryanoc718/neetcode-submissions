class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs[0]):
            for w in range(1, len(strs)):
                if i == len(strs[w]):
                    return strs[0][:i]
                if strs[w][i] != strs[w-1][i]:
                    return strs[0][:i]
            i += 1
        return strs[0]