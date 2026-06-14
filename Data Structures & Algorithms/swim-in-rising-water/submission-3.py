class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        heap = [[0, (0, 0)]]
        visit = {}
        for i in range(row):
            for j in range(col):
                visit[(i, j)] = float("inf")
        def AddCell(i, j, pathMax):
            if i not in range(row) or j not in range(col) or visit[(i, j)] <= pathMax:
                return
            visit[(i, j)] = pathMax
            heapq.heappush(heap, (pathMax, (i, j)))
        while heap:
            pathMax, v = heapq.heappop(heap)
            i, j = v[0], v[1]
            pathMax = max(pathMax, grid[i][j])
            if i == row-1 and j == col-1:
                return pathMax
            AddCell(i-1, j, pathMax)
            AddCell(i+1, j, pathMax)
            AddCell(i, j-1, pathMax)
            AddCell(i, j+1, pathMax)
        return grid[row-1][col-1]
