class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        i = 1
        
        while i < 4 and i < len(s) - 2:
            j = i + 1
            while j < i + 4 and j < len(s) - 1:
                k = j + 1
                while k < j + 4 and k < len(s):
                    s1 = s[0:i]
                    s2 = s[i:j]
                    s3 = s[j:k]
                    s4 = s[k:]
                    if self.isValid(s1) and self.isValid(s2) and self.isValid(s3) and self.isValid(s4):
                        res.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
                    k += 1
                j += 1
            i += 1
                        
        return res
    
    
    def isValid(self, s):
        if len(s) > 3 or len(s) == 0 or int(s) > 255 or (len(s) > 1 and s[0] == '0') :
            return False
        return True