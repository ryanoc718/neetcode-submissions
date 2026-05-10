class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i, j, part, c, seen):
            if word == part:
                return True
            if len(part) >= len(word):
                return False
            seen.add(tuple([i, j]))
            up = False
            if i > 0 and word[c+1] == board[i-1][j] and tuple([i-1, j]) not in seen:
                up = search(i-1, j, part+board[i-1][j], c+1, seen.copy())
            down = False
            if i < len(board)-1 and word[c+1] == board[i+1][j] and tuple([i+1, j]) not in seen:
                down = search(i+1, j, part+board[i+1][j], c+1, seen.copy())
            left = False
            if j > 0 and word[c+1] == board[i][j-1] and tuple([i, j-1]) not in seen:
                left = search(i, j-1, part+board[i][j-1], c+1, seen.copy())
            right = False
            if j < len(board[i])-1 and word[c+1] == board[i][j+1] and tuple([i, j+1]) not in seen:
                right = search(i, j+1, part+board[i][j+1], c+1, seen.copy())
            return up or down or left or right

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if search(i, j, word[0], 0, set()):
                        return True
        return False