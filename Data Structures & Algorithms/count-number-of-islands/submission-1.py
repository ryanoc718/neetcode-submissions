class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        islands = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    print("here")
                    islands += 1
                    dq = deque([(i, j)])
                    while dq:
                        r, c = dq.popleft()
                        if r in range(ROW) and c in range(COL) and grid[r][c] == "1":
                            grid[r][c] = "0"
                            dq.append((r+1,c))
                            dq.append((r-1,c))
                            dq.append((r,c-1))
                            dq.append((r,c+1))
        return islands