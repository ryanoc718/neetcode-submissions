class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        t = r = c = 0
        h = [[grid[0][0],r,c]]
        seen = set()
        while h:
            elevation, r, c = heapq.heappop(h)
            if (r,c) in seen:
                continue
            seen.add((r,c))
            if elevation > t:
                t = elevation
            if r == N-1 and c == N-1:
                return t
            if r-1 in range(N):
                heapq.heappush(h, [grid[r-1][c], r-1, c])
            if r+1 in range(N):
                heapq.heappush(h, [grid[r+1][c], r+1, c])
            if c-1 in range(N):
                heapq.heappush(h, [grid[r][c-1], r, c-1])
            if c+1 in range(N):
                heapq.heappush(h, [grid[r][c+1], r, c+1])
        return 0