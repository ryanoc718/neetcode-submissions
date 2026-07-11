class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s)-1:
                return s[-1] == '0'
            if s[i] == '1' or i >= len(s):
                return False
            dp[i] = False
            for j in range(min(i+maxJump, len(s)-1), i+minJump-1, -1):
                if dfs(j):
                    dp[i] = True
            return dp[i]
        return dfs(0)