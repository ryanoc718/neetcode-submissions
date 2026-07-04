class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                left, up = -1, -1
                if r-1 in range(rows):
                    up = grid[r-1][c]
                if c-1 in range(cols):
                    left = grid[r][c-1]
                if r == 0:
                    grid[r][c] += left
                elif c == 0:
                    grid[r][c] += up
                else:
                    grid[r][c] += min(left, up)
        return grid[-1][-1]