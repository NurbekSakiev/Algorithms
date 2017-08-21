class Solution(object):
    def findTheDifference(self, s, t):
        arr = [0] * 128
        
        for i in s:
            arr[ord(i)] += 1
        
        for j in t:
            if arr[ord(j)] == 0:
                return j
            else:
                arr[ord(j)] -= 1