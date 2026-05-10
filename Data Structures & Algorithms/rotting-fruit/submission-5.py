class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        dq = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    dq.append((r,c))
        if fresh == 0:
            return 0
        time = -1
        while dq:
            if fresh == 0:
                break
            time += 1
            for _ in range(len(dq)):
                r, c = dq.popleft()
                if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                    continue
                if time > 1 and grid[r][c] == 2:
                    continue
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1
                dq.append((r-1, c))
                dq.append((r+1, c))
                dq.append((r, c-1))
                dq.append((r, c+1))
        return time if fresh == 0 else -1

