class Solution(object):
    def generateMatrix(self, n):
        mat = [[0 for i in range(n)] for j in range(n)]
        left, right, upper, bottom = 0, n , 0 , n
        count = 1
        
        while count <= n*n:
            for i in range(left, right):
                mat[upper][i] = count
                count += 1
            upper += 1
            
            for j in range(upper, bottom):
                mat[j][right - 1] = count
                count += 1
                
            right -= 1
            
            if count > n*n:
                break
                
            for i in range(right - 1, left - 1, -1):
                mat[bottom - 1][i] = count
                count += 1
            bottom -= 1
            if count > n*n:
                break
                
            for j in range(bottom - 1, upper - 1, -1):
                mat[j][left] = count
                count += 1
            left += 1
        return mat