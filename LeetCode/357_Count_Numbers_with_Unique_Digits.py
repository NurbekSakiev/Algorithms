class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        unique = 9
        res = 10
        available = 9
        
        while n > 1 and available > 0:
            unique = unique * available
            res += unique
            available -= 1
            n -= 1
        return res