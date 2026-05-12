class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n]*m
        for row in range(m):
            for col in range(n):
                if row != 0 and col != 0:
                    grid[row][col] = grid[row-1][col]+grid[row][col-1]
        return grid[-1][-1]