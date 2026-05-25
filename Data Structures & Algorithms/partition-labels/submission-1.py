class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pairs = {}
        for c in range(len(s)):
            pairs[s[c]] = c
        splits = []
        goal = 0
        length = 0
        for c in range(len(s)):
            goal = max(goal, pairs[s[c]])
            length += 1
            if goal == c:
                splits.append(length)
                length = 0
        return splits