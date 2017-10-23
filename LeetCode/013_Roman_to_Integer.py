class Solution(object):
    def romanToInt(self, s):
        dic = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        res = 0
        for num in s:
            res += dic[num]
        
        if 'IV' in s:
            res -= 2
        if 'IX' in s:
            res -= 2
        if 'XL' in s:
            res -= 20
        if 'XC' in s:
            res -= 20
        if 'CM' in s:
            res -= 200
        if 'CD' in s:
            res -= 200
        return res
        
