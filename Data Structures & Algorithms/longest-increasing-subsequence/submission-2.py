class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, j):
            if i == len(nums):
                return 0
            if (i, j) in dp:
                return dp[(i,j)]
            LIS = dfs(i+1, j)
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1+dfs(i+1, i))
            dp[(i, j)] = LIS
            return dp[(i, j)]
        return dfs(0, -1)
            