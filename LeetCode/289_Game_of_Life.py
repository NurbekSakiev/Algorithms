class Solution(object):
    def gameOfLife(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    if self.totNeighbors(board, i, j) == 3:
                        board[i][j] = 2
                elif board[i][j] == 1:
                    if self.totNeighbors(board, i, j) < 2 or self.totNeighbors(board, i, j) > 3:
                        board[i][j] = 3
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
                
    def totNeighbors(self, board, i, j):
        m, n = len(board), len(board[0])
        tot = 0
        if self.alive(board, m, n, i+1, j):
            tot += 1
        if self.alive(board, m, n, i-1, j):
            tot += 1
        if self.alive(board, m, n, i+1, j+1):
            tot += 1
        if self.alive(board, m, n, i-1, j+1):
            tot += 1
        if self.alive(board, m, n, i+1, j-1):
            tot += 1
        if self.alive(board, m, n, i-1, j-1):
            tot += 1
        if self.alive(board, m, n, i, j+1):
            tot += 1
        if self.alive(board, m, n, i, j-1):
            tot += 1
        return tot
        
    def alive(self,board, m, n, i, j):
        
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        return board[i][j] == 1 or board[i][j] == 3