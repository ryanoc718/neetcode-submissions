class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, steps, visited):
            if r not in range(ROWS) or c not in range(COLS):
                return
            if grid[r][c] <= 0:
                return
            if (r,c) in visited:
                return
            if grid[r][c] <= steps:
                return

            grid[r][c] = steps

            visited.add((r, c))
            dfs(r+1, c, steps+1, visited.copy())
            dfs(r-1, c, steps+1, visited.copy())
            dfs(r, c+1, steps+1, visited.copy())
            dfs(r, c-1, steps+1, visited.copy())

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    dfs(i+1, j, 1, set())
                    dfs(i-1, j, 1, set())
                    dfs(i, j+1, 1, set())
                    dfs(i, j-1, 1, set())

