class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        mat = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        
        curr = [1 for i in range(len(obstacleGrid))]
        prev = [1 for i in range(len(obstacleGrid))]
        
        for j in range(len(obstacleGrid[0])):
            for i in range(len(obstacleGrid)):
                if obstacleGrid[i][j] == 1:
                    curr[i] = 0
                elif i == 0 and j != 0:
                    if prev[i] != 0:
                        curr[i] = 1
                    else:
                        curr[i] = 0
                elif j == 0:
                    if i > 0 and curr[i - 1] == 0:
                        curr[i] = 0
                    else:
                        curr[i] = 1
                else:
                    curr[i] = curr[i-1] + prev[i]
            prev = curr
        
        return prev[i]