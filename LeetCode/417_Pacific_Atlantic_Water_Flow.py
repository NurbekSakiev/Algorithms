class Solution(object):
    def pacificAtlantic(self, matrix):
        if not len(matrix) or not len(matrix[0]):
            return []
        res = []
        n, m = len(matrix), len(matrix[0])
        pac_bool = [[0 for i in range(m)] for j in range(n)]
        at_bool = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            self.dfs(matrix, pac_bool, float('-inf'), i, 0)
            self.dfs(matrix, at_bool, float('-inf'), i, m-1)
        for j in range(m):
            self.dfs(matrix, pac_bool, float('-inf'), 0, j)
            self.dfs(matrix, at_bool, float('-inf'), n-1, j)
            
        for i in range(n):
            for j in range(m):
                if at_bool[i][j] and pac_bool[i][j]:
                    res.append([i,j])
        return res
                    
    def dfs(self, matrix, visited, height, i, j):
        direct = [[0,1],[0,-1],[1,0],[-1,0]]
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or visited[i][j] or matrix[i][j] < height:
            return 1
        visited[i][j] = 1
        for d in direct:
            self.dfs(matrix, visited, matrix[i][j], i + d[0], j + d[1])