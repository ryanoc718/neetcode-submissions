class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        def dfs(i, aliceTurn):
            if (i, aliceTurn) in memo:
                return memo[(i, aliceTurn)]
            if i == len(stoneValue):
                return 0
            if aliceTurn:
                one = two = three = float("-inf")
                if len(stoneValue)-i >= 3:
                    three = dfs(i+3, False) + sum(stoneValue[i:i+3])
                if len(stoneValue)-i >= 2:
                    two = dfs(i+2, False) + sum(stoneValue[i:i+2])
                one = dfs(i+1, False) + stoneValue[i]
                alice = max(one, two, three)
            else:
                one = two = three = float("inf")
                if len(stoneValue)-i >= 3:
                    three = dfs(i+3, True) - sum(stoneValue[i:i+3])
                if len(stoneValue)-i >= 2:
                    two = dfs(i+2, True) - sum(stoneValue[i:i+2])
                one = dfs(i+1, True) - stoneValue[i]
                alice = min(one, two, three)
            memo[(i, aliceTurn)] = alice
            return alice
        res = dfs(0, True)
        if res == 0:
            return "Tie"
        if res > 0:
            return "Alice"
        return "Bob"

                