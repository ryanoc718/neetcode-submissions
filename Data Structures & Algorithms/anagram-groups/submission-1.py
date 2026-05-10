class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            chars = [0]*26
            for c in word:
                chars[ord(c)-ord('a')] += 1
            if tuple(chars) in groups:
                groups[tuple(chars)].append(word)
            else:
                groups[tuple(chars)] = [word]
        return list(groups.values())
            