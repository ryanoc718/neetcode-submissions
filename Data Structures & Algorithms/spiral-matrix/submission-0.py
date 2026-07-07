class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        visited = set()
        dMap = {"r":"d", "d":"l", "l":"u", "u":"r"}
        direction = "r"
        r, c = 0, 0
        while len(res) < (rows*cols):
            if (r, c) not in visited:
                visited.add((r, c))
                res.append(matrix[r][c])
            if direction == "r":
                if (r, c+1) in visited or c+1 not in range(cols):
                    direction = dMap[direction]
                    continue
                c += 1
            elif direction == "d":
                if (r+1, c) in visited or r+1 not in range(rows):
                    direction = dMap[direction]
                    continue
                r += 1
            elif direction == "l":
                if (r, c-1) in visited or c-1 not in range(cols):
                    direction = dMap[direction]
                    continue
                c -= 1
            else:
                if (r-1, c) in visited or r-1 not in range(rows):
                    direction = dMap[direction]
                    continue
                r -= 1
        return res
            