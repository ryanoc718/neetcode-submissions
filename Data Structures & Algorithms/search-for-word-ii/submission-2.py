class TrieNode:
    def __init__(self):
        self.childs = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for w in word:
                if w not in cur.childs:
                    cur.childs[w] = TrieNode()
                cur = cur.childs[w]
            cur.end = True
        
        resSet = set()
        def search(prefix, node, prev, row, col):
            prefix += board[row][col]
            if node.end:
                resSet.add(prefix)
            prev.add(tuple((row, col)))

            if row > 0 and tuple((row-1, col)) not in prev and board[row-1][col] in node.childs: # up
                search(prefix, node.childs[board[row-1][col]], prev.copy(), row-1, col)
            if row < len(board)-1 and tuple((row+1, col)) not in prev and board[row+1][col] in node.childs: # down
                search(prefix, node.childs[board[row+1][col]], prev.copy(), row+1, col)
            if col > 0 and tuple((row, col-1)) not in prev and board[row][col-1] in node.childs: # left
                search(prefix, node.childs[board[row][col-1]], prev.copy(), row, col-1)
            if col < len(board[row])-1 and tuple((row, col+1)) not in prev and board[row][col+1] in node.childs: # right
                search(prefix, node.childs[board[row][col+1]], prev.copy(), row, col+1)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in root.childs:
                    search("", root.childs[board[i][j]], set(), i, j)
        return list(resSet)
                





