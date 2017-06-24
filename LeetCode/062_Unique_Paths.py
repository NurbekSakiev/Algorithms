class Solution(object):

    def uniquePaths(self, m, n):
        mat = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(n):
            mat[0][i] = 1
        for j in range(m):
            mat[j][0] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
            
        return mat[-1][-1]

#Solution 2

    def uniquePaths(self, m, n):
        mat = [[0 for i in range(n)] for j in range(m)]
        
        prev = [1 for i in range(m)]
        curr = [1 for j in range(m)]
        
        for i in range(1,n):
            curr[0] = 1
            for j in range(1,m):
                curr[j] = curr[j-1] + prev[j]
            prev = curr
        return prev[-1]