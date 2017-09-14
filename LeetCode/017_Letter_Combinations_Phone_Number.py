class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        dic = ['0', '1','abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = [""]
        for i in range(len(digits)):
            x = int(digits[i])
            while len(res[-1]) == i:
                t = res.pop()
                for s in list(dic[x]):
                    res.insert(0,t + s)
        return res

# Solution 2

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0: return []
        return [a + b for a in self.letterCombinations(digits[:-1]) 
                      for b in self.letterCombinations(digits[-1])] or list(dic[digits])