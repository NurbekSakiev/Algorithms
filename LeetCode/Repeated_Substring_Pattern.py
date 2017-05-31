class Solution(object):
    def repeatedSubstringPattern(self, s):
        i = 0
        sLen = len(s)
        if sLen < 2:
            return False
        while i < sLen/2:
            i += 1
            if sLen % (i) != 0:
                continue
            newStr = s[:i]
            checkStr = newStr * (sLen / i)
            if s == checkStr:
                return True
        return False