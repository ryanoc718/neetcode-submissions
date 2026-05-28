class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0]*(len(text2)+1)
        for i in range(len(text1)-1, -1, -1):
            nextDp = [0]*(len(text2)+1)
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    nextDp[j] = 1 + dp[j+1]
                else:
                    nextDp[j] = max(dp[j], nextDp[j+1])
            dp = nextDp
        return dp[0]