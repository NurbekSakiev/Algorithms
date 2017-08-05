class Solution(object):
    def minWindow(self, s, t):
        start, end = 0, 0 
        minLen = sys.maxint
        dic = [0 for i in range(128)]
        minStart = 0
        
        for i in t:
            dic[ord(i)] += 1
        count = len(t)
        
        while end < len(s):
            if dic[ord(s[end])] > 0:
                count -= 1
            dic[ord(s[end])] -= 1
            while count == 0:
                if end - start + 1 < minLen:
                    minLen = end - start + 1
                    minStart = start
                dic[ord(s[start])] += 1
                if dic[ord(s[start])] > 0:
                    count += 1
                start += 1
            end += 1
        return "" if minLen == sys.maxint else s[minStart:minStart + minLen]