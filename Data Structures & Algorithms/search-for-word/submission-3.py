class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visit = set()
        def dfs(r, c, w):
            if w == word:
                return True
            if (r, c) in visit:
                return False
            if r not in range(row) or c not in range(col) or w != word[:len(w)]:
                return False
            w += board[r][c]
            visit.add((r, c))
            res = (dfs(r-1, c, w) or
            dfs(r+1, c, w) or
            dfs(r, c-1, w) or
            dfs(r, c+1, w))
            visit.remove((r,c))
            return res
        for i in range(row):
            for j in range(col):
                if dfs(i, j, ""):
                    return True
        return False
            
            
            