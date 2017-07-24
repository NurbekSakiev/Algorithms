class Solution(object):
    def rotate(self, matrix):
        
        n = len(matrix)
        
        for i in range(n/2):
            for j in range(n - (2*i) - 1):
                temp = matrix[j + i][n-i-1]
                print temp
                matrix[j + i][n-i-1] = matrix[i][j + i]
                matrix[i][j + i] = matrix[n - 1 - i - j][i]
                matrix[n - 1 - i - j][i] = matrix[n - i - 1][n - 1 - i - j]
                matrix[n - i - 1][n - i - 1 - j] = temp


# Solution 2

    def rotate(self, matrix):
        
        s, e = 0, len(matrix) - 1
        
        while s < e:
            temp = matrix[s]
            matrix[s] = matrix[e]
            matrix[e] = temp
            s += 1
            e -= 1
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp