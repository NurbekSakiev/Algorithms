class Solution(object):
    def checkInclusion(self, s1, s2):
        arr = [0] * 128
        
        for i in s1:
            arr[ord(i)] += 1
        
        count = len(s1)
        
        start, end = 0, 0
        
        while end < len(s2):
            if arr[ord(s2[end])] > 0:
                count -= 1
            arr[ord(s2[end])] -= 1
            while count == 0:
                if end - start == len(s1) - 1:
                    return True 
                arr[ord(s2[start])] += 1
                if arr[ord(s2[start])] > 0:
                    count += 1
                start += 1
            end += 1
        return False