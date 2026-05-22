class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        chests = []
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    chests.append((i,j))
        dq = deque(chests)
        dist = -1
        while dq:
            dist += 1
            for _ in range(len(dq)):
                i, j = dq.popleft()
                if i not in range(ROW) or j not in range(COL):
                    continue
                if grid[i][j] < dist:
                    continue
                grid[i][j] = dist
                dq.append((i+1, j))
                dq.append((i-1, j))
                dq.append((i, j+1))
                dq.append((i, j-1))


