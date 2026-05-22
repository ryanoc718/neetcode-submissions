class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(dp[-1])-1, -1, -1):
            dp[-1][i] = len(dp[-1])-(i+1)
        for i in range(len(dp)-1, -1, -1):
            dp[i][-1] = len(dp)-(i+1)
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word2[j] == word1[i]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1+min(dp[i+1][j], dp[i+1][j+1], dp[i][j+1])
        return dp[0][0]