class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [[grid[0][0], 0, 0]]
        seen = set()
        while heap:
            cost, r, c = heapq.heappop(heap)
            if r not in range(rows) or c not in range(cols):
                continue
            seen.add((r, c))
            if r == rows-1 and c == cols-1:
                return cost
            if r+1 in range(rows) and (r+1, c) not in seen:
                heapq.heappush(heap, [grid[r+1][c]+cost, r+1, c])
            if c+1 in range(cols) and (r, c+1) not in seen:
                heapq.heappush(heap, [grid[r][c+1]+cost, r, c+1])
        return grid[0][0]
