class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        copy = []
        #Pacific BFS
        dq = deque()
        for i in range(ROWS):
            copy.append([])
            for j in range(COLS):
                if i == 0 or j == 0:
                    dq.append([i, j, -1])
                copy[i].append(0)
        visited = set()
        while dq:
            r, c, prev = dq.popleft()
            if r not in range(ROWS) or c not in range(COLS):
                continue
            if (r,c) in visited:
                continue
            if heights[r][c] < prev:
                continue
            visited.add((r,c))
            copy[r][c] += 1
            h = heights[r][c]
            dq.append([r-1, c, h])
            dq.append([r+1, c, h])
            dq.append([r, c-1, h])
            dq.append([r, c+1, h])
        #Atlantic BFS
        dq = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if i == ROWS-1 or j == COLS-1:
                    dq.append([i, j, -1])
        visited = set()
        while dq:
            r, c, prev = dq.popleft()
            if r not in range(ROWS) or c not in range(COLS):
                continue
            if (r,c) in visited:
                continue
            if heights[r][c] < prev:
                continue
            visited.add((r,c))
            copy[r][c] += 1
            h = heights[r][c]
            dq.append([r-1, c, h])
            dq.append([r+1, c, h])
            dq.append([r, c-1, h])
            dq.append([r, c+1, h])
        for r in range(ROWS):
            for c in range(COLS):
                if copy[r][c] == 2:
                    res.append([r,c])
        return res

