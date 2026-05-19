class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(one, two, three):
            if one >= len(s1) and two >= len(s2):
                memo[(one, two)] = True
                return True
            if three == len(s3):
                memo[(one, two)] = False
                return False
            if (one, two) in memo:
                return memo[(one, two)]
            pickOne, pickTwo = False, False
            if one < len(s1) and s1[one] == s3[three]:
                memo[(one, two)] = pickOne = dfs(one+1, two, three+1)
            if two < len(s2) and s2[two] == s3[three]:
                memo[(one, two)] = pickTwo = dfs(one, two+1, three+1)
            return pickOne or pickTwo
        return dfs(0,0,0) and len(s1)+len(s2) == len(s3)