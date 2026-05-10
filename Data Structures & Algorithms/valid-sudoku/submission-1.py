class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]

        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                num = board[row][col]
                if num != ".":
                    #print(sqrs)
                    if num in rows[row]:
                        return False
                    if num in cols[col]:
                        return False
                    rows[row].add(num)
                    cols[col].add(num)
                    if row < 3 and col < 3: #0
                        if num in sqrs[0]:
                            return False
                        sqrs[0].add(num)
                        continue
                    elif row < 3 and col< 6: #1
                        if num in sqrs[1]:
                            return False
                        sqrs[1].add(num)
                        continue
                    elif row < 3 and col < 9: #2
                        if num in sqrs[2]:
                            return False
                        sqrs[2].add(num)
                        continue
                    elif row < 6 and col < 3: #3
                        if num in sqrs[3]:
                            return False
                        sqrs[3].add(num)
                        continue
                    elif row < 6 and col < 6: #4
                        if num in sqrs[4]:
                            return False
                        sqrs[4].add(num)
                        continue
                    elif row < 6 and col < 9: #5
                        if num in sqrs[5]:
                            return False
                        sqrs[5].add(num)
                        continue
                    elif col < 3: #6
                        if num in sqrs[6]:
                            return False
                        sqrs[6].add(num)
                        continue
                    elif col < 6: #7
                        if num in sqrs[7]:
                            return False
                        sqrs[7].add(num)
                        continue
                    elif num in sqrs[8]: #8
                        return False
                    sqrs[8].add(num)
        return True