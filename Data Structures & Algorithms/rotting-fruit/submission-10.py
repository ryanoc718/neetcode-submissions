class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        fresh = 0
        row, col = len(grid), len(grid[0])
        def AddCell(i, j):
            if i not in range(row) or j not in range(col) or grid[i][j] != 1:
                return
            q.append((i, j))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    AddCell(i-1, j)
                    AddCell(i+1, j)
                    AddCell(i, j-1)
                    AddCell(i, j+1)
        time = 0
        while q:
            rot = False
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] != 1:
                    continue
                fresh -= 1
                rot = True
                grid[r][c] = 2
                AddCell(r-1, c)
                AddCell(r+1, c)
                AddCell(r, c-1)
                AddCell(r, c+1)
            if rot:
                time += 1
        if fresh <= 0:
            return time
        return -1

                
