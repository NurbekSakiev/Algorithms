class Solution(object):
    def generateParenthesis(self, n):
        res = []
        self.back(res, "", 0, 0, n)
        return res
        
    def back(self, res, newStr, opener, closer, maxN):
        if len(newStr) == 2 * maxN:
            res.append(newStr)
            return
        print res, newStr, opener, closer
        if opener < maxN:
            self.back(res, newStr + '(', opener + 1, closer, maxN)
        if closer < opener:
            self.back(res, newStr + ')', opener, closer + 1, maxN)