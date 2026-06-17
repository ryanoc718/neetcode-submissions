class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visit = set()
        def dfs(r, c, w):
            if w == len(word):
                return True
            if r not in range(row) or c not in range(col) or (r, c) in visit or board[r][c] != word[w]:
                return False
            w += 1
            visit.add((r, c))
            res = (dfs(r-1, c, w) or
            dfs(r+1, c, w) or
            dfs(r, c-1, w) or
            dfs(r, c+1, w))
            visit.remove((r,c))
            return res
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False