class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(ROWS):
            for j in range(COLS):
                obstacleGrid[i][j] *= -1
        obstacleGrid[0][0] = 1
        for i in range(ROWS):
            for j in range(COLS):
                if obstacleGrid[i][j] == -1:
                    continue
                if i-1 in range(ROWS) and obstacleGrid[i-1][j] >= 0:
                    obstacleGrid[i][j] += obstacleGrid[i-1][j]
                if j-1 in range(COLS) and obstacleGrid[i][j-1] >= 0:
                    obstacleGrid[i][j] += obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]