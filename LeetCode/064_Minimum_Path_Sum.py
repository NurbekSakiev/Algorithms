class Solution(object):

    def minPathSum(self, grid):
        mat = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        mat[0][0] = grid[0][0]
        
        for i in range(1,len(grid)):
            mat[i][0] = mat[i-1][0] + grid[i][0]
        
        for j in range(1,len(grid[0])):
            mat[0][j] = mat[0][j-1] + grid[0][j]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + grid[i][j]
            
        return mat[len(mat) - 1][len(mat[0]) - 1]


    def minPathSum(self, grid):
        
        curr = [0 for i in range(len(grid))]
        
        prev = [0 for i in range(len(grid))]
        prev[0] = grid[0][0]
        
        for i in range(1,len(prev)):
            prev[i] = prev[i-1] + grid[i][0]
        
        for i in range(1, len(grid[0])):
            curr[0] = prev[0] + grid[0][i]
            for j in range(1, len(grid)):
                curr[j] = min(curr[j-1], prev[j]) + grid[j][i]
            prev = curr
        
        return prev[-1]