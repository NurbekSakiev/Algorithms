class Solution(object):
    def updateMatrix(self, matrix):
        out = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    self.bfs(matrix, out, i, j)
                
        return out
            
        
    def bfs(self, matrix, out, i, j):
        q = [[[i,j], 0]]
        or_i, or_j = i,j
        while q:
            point = q.pop()
            i, j, level = point[0][0], point[0][1], point[1]
            if i < 0 or i == len(matrix) or j < 0 or j == len(matrix[0]):
                continue
            if matrix[i][j] == 0:
                out[or_i][or_j] = level
                return
            q.insert(0,[[i + 1, j], level + 1])
            q.insert(0,[[i - 1, j], level + 1])
            q.insert(0,[[i, j + 1], level + 1])
            q.insert(0,[[i, j - 1], level + 1])