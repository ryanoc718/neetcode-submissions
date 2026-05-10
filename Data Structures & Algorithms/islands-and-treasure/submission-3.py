class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c, steps):
            if r not in range(ROWS) or c not in range(COLS):
                return
            if grid[r][c] <= 0:
                return
            if grid[r][c] <= steps:
                return

            grid[r][c] = steps
            dfs(r+1, c, steps+1)
            dfs(r-1, c, steps+1)
            dfs(r, c+1, steps+1)
            dfs(r, c-1, steps+1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    dfs(i+1, j, 1)
                    dfs(i-1, j, 1)
                    dfs(i, j+1, 1)
                    dfs(i, j-1, 1)

