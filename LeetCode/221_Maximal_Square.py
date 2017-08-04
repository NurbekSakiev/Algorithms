class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        maxSq = 0
        
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    maxSq = max(maxSq, dp[i][j])
        
        return maxSq * maxSq

# Solution 2 (space complexity)


    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        prev = [0 for i in range(len(matrix) + 1)]
        
        maxSq = 0
        
        for j in range(1, len(matrix[0]) + 1):
            curr = [0 for i in range(len(matrix) + 1)]
            for i in range(1, len(matrix) + 1):
                if matrix[i-1][j-1] == "1":
                    curr[i] = min(curr[i-1], prev[i-1], prev[i]) + 1
                    maxSq = max(maxSq, curr[i])
            prev = curr
        
        return maxSq * maxSq