class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        seen = set()
        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                if r not in range(row) or c not in range(col) or (
                    board[r][c] == "X" or (r, c) in seen):
                    continue
                seen.add((r, c))
                q.append((r+1, c))
                q.append((r-1, c))
                q.append((r, c-1))
                q.append((r, c+1))

        for i in range(row):
            bfs(i, 0)
            bfs(i, col-1)
        for i in range(col):
            bfs(0, i)
            bfs(row-1, i)
        for i in range(row):
            for j in range(col):
                if (i, j) not in seen:
                    board[i][j] = "X"
