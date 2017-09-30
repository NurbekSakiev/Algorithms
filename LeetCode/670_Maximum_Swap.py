class Solution(object):
    def maximumSwap(self, num):
        s = list(str(num))
        stack = []
        maxNum = float('-inf')
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) > maxNum:
                maxNum = int(s[i])
                idx = i
            stack.append([maxNum, idx])
            
        for j in range(len(s) - 1):
            maxNum = stack[-1][0]; idx = stack[-1][1]
            if int(s[j]) < maxNum and j < idx:
                s[j], s[idx] = s[idx], s[j]
                return int(''.join(s))
            stack.pop()
        return num