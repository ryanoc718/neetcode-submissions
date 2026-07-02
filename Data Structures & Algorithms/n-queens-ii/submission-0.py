class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for _ in range(n)]
        def isSafe(r, c):
            left, right = c-1, c+1
            for row in range(r-1, -1, -1):
                if board[row][c] == 1:
                    return False
                if left >= 0 and board[row][left] == 1:
                    return False
                if right < n and board[row][right] == 1:
                    return False
                left -= 1
                right += 1
            return True
        def backtrack(r):
            if r == n:
                return 1
            res = 0
            for c in range(n):
                if isSafe(r, c):
                    board[r][c] = 1
                    res += backtrack(r+1)
                    board[r][c] = 0
            return res
        return backtrack(0)



            
