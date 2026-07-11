class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False]*(len(s))
        dp[-1] = s[-1] == '0'
        for i in range(len(s)-1, -1, -1):
            for j in range(min(i+maxJump, len(s)-1), i+minJump-1, -1):
                dp[i] = dp[j] and s[j] != '1'
                if dp[i]:
                    break
        return dp[0]