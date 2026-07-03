class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zrow, zcol = set(), set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zrow.add(r)
                    zcol.add(c)
        for r in zrow:
            for c in range(len(matrix[r])):
                matrix[r][c] = 0
        for c in zcol:
            for r in range(len(matrix)):
                matrix[r][c] = 0
        