class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j, prev):
            if i not in range(ROW) or j not in range(COL):
                return 0
            if prev[0] != -1 and matrix[i][j] <= matrix[prev[0]][prev[1]]:
                return 0
            if (i, j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = 1 + max(dfs(i-1,j,(i,j)), dfs(i+1,j,(i,j)), dfs(i,j-1,(i,j)), dfs(i,j+1,(i,j)))
            return dp[(i,j)]
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                res = max(dfs(r, c, (-1,-1)), res)
        return res
