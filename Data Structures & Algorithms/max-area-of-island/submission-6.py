class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROW, COL = len(grid), len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    dq = deque([(i, j)])
                    cur = 0
                    while dq:
                        r, c = dq.popleft()
                        if r not in range(ROW) or c not in range(COL) or grid[r][c] != 1:
                            continue
                        grid[r][c] = 0
                        cur += 1
                        dq.append((r-1, c))
                        dq.append((r+1, c))
                        dq.append((r, c-1))
                        dq.append((r, c+1))
                    area = max(area, cur)
        return area
                        