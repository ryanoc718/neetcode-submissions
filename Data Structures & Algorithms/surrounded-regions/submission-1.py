class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        seen = set()
        def dfs(i, j):
            if i not in range(row) or j not in range(col) or (
                board[i][j] == "X" or (i, j) in seen):
                return
            seen.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        for i in range(col):
            dfs(0, i)
            dfs(row-1, i)
        for i in range(row):
            for j in range(col):
                if (i, j) not in seen:
                    board[i][j] = "X"
