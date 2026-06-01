class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        dq = deque()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    dq.append((i, j))
        dist = 0
        seen = set()
        while dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                if r not in range(ROW) or c not in range(COL) or (
                    grid[r][c] < 0 or (r, c) in seen):
                    continue
                seen.add((r,c))
                grid[r][c] = dist
                dq.append((r-1,c))
                dq.append((r+1,c))
                dq.append((r,c-1))
                dq.append((r,c+1))
            dist += 1
