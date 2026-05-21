class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = {}
        def dfs(ss, i):
            if (ss, i) in dp:
                return dp[(ss, i)]
            if ss == t: 
                return 1
            if len(ss) >= len(t) or i >= len(s) or ss != t[:len(ss)]:
                return 0
            dp[(ss, i)] = dfs(ss+s[i], i+1) + dfs(ss, i+1) 
            return dp[(ss, i)]
        return dfs("", 0)

