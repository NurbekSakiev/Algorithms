res = 0
class Solution(object):
    def countSubstrings(self, s):
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            self.extendPalin(s, i, i)
            self.extendPalin(s, i, i + 1)
        return res
        
    def extendPalin(self, s, left, right):
        global res
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1