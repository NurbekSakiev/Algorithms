class Solution(object):
    def reverseWords(self, s):
        start, end = 0,0
        s = list(s)
        i = 0
        while i < len(s):
            if s[i] == ' ':
                self.reverseWord(start, end-1, s)
                while s[i] == ' ':
                    i += 1
                start = i
            elif i == len(s) - 1:
                self.reverseWord(start, end, s)
            i += 1
            end = i
        i,j = 0,0
        while i < len(s):
            while i < len(s) and s[i] != ' ':
                s[j] = s[i]
                j += 1
                i += 1
            i += 1
        return ''.join(map(str,s[:j]))
    
    def reverseWord(self, start, end, s):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1