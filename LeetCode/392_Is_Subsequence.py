class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        ptrS = 0
        ptrT = 0
        
        while ptrT < len(t):
            if s[ptrS] == t[ptrT]:
                ptrS += 1
                if ptrS == len(s):
                    return True
            ptrT += 1
        return False