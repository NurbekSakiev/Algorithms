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

# Solution 2 


    def maximumSwap(self, num):
        
        num_list = map(int, str(num))
        dic = {x:i for i, x in enumerate(num_list)}
        for i, x in enumerate(num_list):
            for k in xrange(9, x, -1):
                if dic.get(k, None) > i:
                    num_list[i], num_list[dic[k]] = num_list[dic[k]], num_list[i]
                    return int(''.join(map(str, num_list)))
        return num