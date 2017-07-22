class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.expand(grid, i, j)
                    count += 1
        return count
    
    def expand(self, grid, i, j):
        q = [[i,j]]
        while any(q):
            coor = q.pop()
            y, x = coor[0], coor[1]
            if grid[y][x] == '1':
                grid[y][x] = '0'
                self.check(grid, y, x + 1, q)
                self.check(grid, y, x - 1, q)
                self.check(grid, y + 1, x, q)
                self.check(grid, y - 1, x, q)
        return

    def check(self, grid, y, x, q):
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            return
        q.append([y,x])

# Solution 2

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.expand(grid, i, j)
                    count += 1
        return count
    
    def expand(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.expand(grid, i, j + 1)
        self.expand(grid, i, j - 1)
        self.expand(grid, i + 1, j)
        self.expand(grid, i - 1, j)