res = 0
class Solution(object):
    def canBeBroken(self, board):
        
        dic = {'bath':1, 'take':1, 'hand':1, 'bat':1, 'come':1, 'and':1}
        self.helper(dic, "takebathandcome")
        return res
    
    def helper(self, dic, s):
        global res
        if len(s) == 0:
            return True
        for i in range(1, len(s) + 1):
            word = s[:i]
            if word in dic and self.helper(dic, s[i:]):
                res += 1
        return False