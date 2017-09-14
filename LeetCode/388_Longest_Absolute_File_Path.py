class Solution(object):
    def lengthLongestPath(self, input):
        tokens = input.split('\n')
        maxLen = 0
        stack = []
        curLen = 0
        
        for s in tokens:
            lev = self.countLevel(s)
            while lev < len(stack):
                curLen -= stack.pop()
            ln = len(s.replace("\t", "")) + 1
            curLen += ln
            if '.' in s:
                maxLen = max(curLen - 1, maxLen)
            stack.append(ln)
        return maxLen
            
        
        
    def countLevel(self, s):
        curr = s.replace("\t", "")
        return len(s) - len(curr)