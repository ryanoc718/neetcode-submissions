class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        m = 0
        area = 0
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] != 1:
                return
            grid[r][c] = 0
            nonlocal m, area
            area += 1
            m = max(area, m)

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
        return m