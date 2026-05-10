class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS):
                return 0
            if grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return 1+(dfs(r-1, c)+
            dfs(r+1, c)+
            dfs(r, c-1)+
            dfs(r, c+1))
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res
