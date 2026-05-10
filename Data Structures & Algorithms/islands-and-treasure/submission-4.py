class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r not in range(ROWS) or c not in range(COLS):
                    continue
                if grid[r][c] < 0 or grid[r][c] < dist:
                    continue

                grid[r][c] = min(dist, grid[r][c])
                q.append((r+1, c))
                q.append((r-1, c))
                q.append((r, c+1))
                q.append((r, c-1))
            dist += 1

                


        