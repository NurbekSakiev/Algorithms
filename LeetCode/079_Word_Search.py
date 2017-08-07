class Solution(object):
    def exist(self, board, word):
        if len(board) == 0 or len(board[0]) == 0:
            return word == ""
        
        w = list(word)
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.back(board, i, j, word, 0, visited):
                    return True
        return False
                    
                    
    def back(self, board, i, j, word, ind, visited):
        if ind == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[ind] or visited[i][j]:
            return False
        
        visited[i][j] = True
        
        if self.back(board, i + 1, j, word, ind + 1, visited) or self.back(board, i - 1, j, word, ind + 1, visited) or self.back(board, i, j + 1, word, ind + 1, visited) or self.back(board, i, j - 1, word, ind + 1, visited):
            return True
        
        visited[i][j] = False
        return False
    
        