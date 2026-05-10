class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        freshFruit = set()
        dq = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    dq.append((r, c))
                elif grid[r][c] == 1:
                    freshFruit.add((r,c))
        if not freshFruit and not dq: return 0
        minute = -1
        def AddSpace(r, c):
            if r not in range(ROWS) or c not in range(COLS):
                return
            if grid[r][c] != 1:
                return
            dq.append((r,c))
            freshFruit.remove((r,c))
            grid[r][c] = 2
        while dq:
            minute += 1
            for i in range(len(dq)):
                r, c = dq.popleft()
                AddSpace(r+1, c)
                AddSpace(r-1, c)
                AddSpace(r, c-1)
                AddSpace(r, c+1)
                    
        if freshFruit: return -1
        print(grid)
        return minute
            

