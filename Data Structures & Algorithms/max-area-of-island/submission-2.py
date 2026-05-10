class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        m = 0
        def bfs(r, c):
            nonlocal m
            area = 0
            dq = deque()
            dq.append([r,c])
            while dq:
                for i in range(len(dq)):
                    nr, nc = dq.popleft()
                    if nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 0
                    area += 1
                    m = max(area, m)
                    dq.append([nr-1, nc])
                    dq.append([nr+1, nc])
                    dq.append([nr, nc-1])
                    dq.append([nr, nc+1])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = 0
                    bfs(i, j)
        return m