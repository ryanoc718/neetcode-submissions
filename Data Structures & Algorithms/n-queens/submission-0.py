class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(board, row, col):
            if col >= n or row-1 >= n:
                return
            r, c = row-1, col
            while r > 0 and c > 0: # back left
                if board[r-1][c-1] == "Q":
                    return
                r -= 1
                c -= 1
            r, c = row-1, col
            while r > 0 and c < n-1: # back right
                if board[r-1][c+1] == "Q":
                    return
                r -= 1
                c += 1
            r, c = row-1, col
            while r > 0: # col
                if board[r-1][c] == "Q":
                    return
                r -= 1
            r, c = row-1, col
            while c > 0: # row
                if board[r][c-1] == "Q":
                    return
                c -= 1

            if len(board) == n:
                temp = []
                for b in board:
                    temp.append(b.copy())
                res.append(temp.copy())

            level = []
            for i in range(n):
                level.append(".")
            board.append(level)
            for i in range(n):
                board[row][i] = "Q"
                backtrack(board.copy(), row+1, i)
                board[row][i] = "."
        backtrack([], 0, 0)
        resString = []
        for r in res:
            board = []
            for level in r:
                b = "".join(level)
                board.append(b)
            resString.append(board)
        return resString