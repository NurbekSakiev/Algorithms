class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        
        begin, end = 0, m * n - 1
        
        while begin <= end:
            mid = (begin + end) / 2
            
            if matrix[mid / n][mid % n] == target:
                return True
                
            elif matrix[mid / n][mid % n] < target:
                begin = mid + 1
            else:
                end = mid - 1
        
        return False
