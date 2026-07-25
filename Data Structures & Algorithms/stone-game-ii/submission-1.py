class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def dfs(aTurn, i, M):
            if (aTurn, (i, M)) in memo:
                return memo[(aTurn, (i, M))]
            if i >= len(piles):
                return 0
            res = 0 if aTurn else float("inf")
            x = 0
            if aTurn:
                stones = 0
                for j in range(i, min(i+(2*M), len(piles))):
                    stones += piles[j]
                    x += 1
                    res = max(res, stones+dfs(False, j+1, max(M, x)))
            else:
                for j in range(i, min(i+(2*M), len(piles))):
                    x += 1
                    res = min(res, dfs(True, j+1, max(M, x)))
            memo[(aTurn, (i, M))] = res
            return res
        return dfs(True, 0, 1)
