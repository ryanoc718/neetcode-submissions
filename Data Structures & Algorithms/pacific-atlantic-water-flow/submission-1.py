class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p, a = set(), set()
        pq = deque([])
        row, col = len(heights), len(heights[0])
        
        for c in range(col):
            pq.append(((row-1, c), -1))
        for r in range(row):
            pq.append(((r, col-1), -1))
        while pq:
            (r, c), prev = pq.popleft()
            if (r, c) in p or r not in range(row) or c not in range(col):
                continue
            if heights[r][c] < prev:
                continue
            p.add((r, c))
            pq.append(((r-1, c), heights[r][c]))
            pq.append(((r+1, c), heights[r][c]))
            pq.append(((r, c-1), heights[r][c]))
            pq.append(((r, c+1), heights[r][c]))
                
        aq = deque([])  
        for c in range(col):
            aq.append(((0, c), -1))
        for r in range(row):
            aq.append(((r, 0), -1))
        while aq:
            (r, c), prev = aq.popleft()
            if (r, c) in a or r not in range(row) or c not in range(col):
                continue
            if heights[r][c] < prev:
                continue
            a.add((r, c))
            aq.append(((r-1, c), heights[r][c]))
            aq.append(((r+1, c), heights[r][c]))
            aq.append(((r, c-1), heights[r][c]))
            aq.append(((r, c+1), heights[r][c]))
        res = set()
        for r, c in p:
            if (r, c) in a:
                res.add((r,c))
        return list(res)
