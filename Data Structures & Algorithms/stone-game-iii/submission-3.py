class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [[0]*2 for _ in range((len(stoneValue)+3))]
        for i in range(len(stoneValue)-1, -1, -1):
            for at in [False, True]:
                if at:
                    one = two = three = float("-inf")
                    if len(stoneValue)-i >= 3:
                        three = dp[i+3][0] + sum(stoneValue[i:i+3])
                    if len(stoneValue)-i >= 2:
                        two = dp[i+2][0] + sum(stoneValue[i:i+2])
                    one = dp[i+1][0] + stoneValue[i]
                    dp[i][at] = max(one, two, three)
                else:
                    one = two = three = float("inf")
                    if len(stoneValue)-i >= 3:
                        three = dp[i+3][1] - sum(stoneValue[i:i+3])
                    if len(stoneValue)-i >= 2:
                        two = dp[i+2][1] - sum(stoneValue[i:i+2])
                    one = dp[i+1][1] - stoneValue[i]
                    dp[i][at] = min(one, two, three)
        res = dp[0][1]
        if res == 0:
            return "Tie"
        if res > 0:
            return "Alice"
        return "Bob"
                