class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        l, r, u, d = 0, len(matrix[0]), 0, len(matrix)
        
        while len(res) < len(matrix[0]) * len(matrix):
    
            for i in range(l, r):
                res.append(matrix[u][i])
            
            u += 1
            
            for j in range(u, d):
                res.append(matrix[j][r - 1])
            
            r -= 1
            
            if len(res) >= len(matrix[0]) * len(matrix):
                break
            
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[d - 1][i])
            d -= 1
            
            if len(res) >= len(matrix[0]) * len(matrix):
                break
            
            for j in range(d - 1, u - 1, -1):
                res.append(matrix[j][l])
            l += 1
            
        return res