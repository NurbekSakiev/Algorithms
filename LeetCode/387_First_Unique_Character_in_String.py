class Solution(object):
    def firstUniqChar(self, s):
        
        chars = [0] * 128
        for i in s:
            chars[ord(i)] += 1
        
        for i in range(len(s)):
            if chars[ord(s[i])] == 1:
                return i
        return -1