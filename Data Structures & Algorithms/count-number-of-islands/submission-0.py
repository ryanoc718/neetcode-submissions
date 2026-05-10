class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(row, col, visited):
            if row == ROWS or col == COLS or row < 0 or col < 0:
                return
            if (row, col) in visited:
                return
            if grid[row][col] == "0":
                return
            
            visited.add(tuple((row, col)))
            grid[row][col] = "0"
            dfs(row-1, col, visited)
            dfs(row+1, col, visited)
            dfs(row, col-1, visited)
            dfs(row, col+1, visited)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j, set())
        return islands
            