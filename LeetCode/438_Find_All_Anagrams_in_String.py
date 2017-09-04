class Solution(object):
    def findAnagrams(self, s, p):
        start = 0; end = 0
        arr = [0] * 128
        count = len(p)
        res = []
        
        for i in p:
            arr[ord(i)] += 1
            
        while end < len(s):
            if arr[ord(s[end])] > 0:
                count -= 1
            arr[ord(s[end])] -= 1
            if count == 0:
                res.append(start)
            end += 1
            if end - start >= len(p):
                arr[ord(s[start])] += 1
                if arr[ord(s[start])] > 0:
                    count += 1
                start += 1
            
        return res