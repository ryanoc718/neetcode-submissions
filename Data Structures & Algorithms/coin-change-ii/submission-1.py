class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        for i in range(len(coins)-1, -1, -1):
            temp = [0]*(amount+1)
            for j in range(amount, -1, -1):
                if j == amount:
                    temp[j] = 1
                elif j+coins[i] <= amount:
                    temp[j] = dp[j] + temp[j+coins[i]]
                else:
                    temp[j] = dp[j]
            dp = temp
        return dp[0]