class Solution(object):
    def fourSumCount(self, A, B, C, D):
        count = 0
        dictAB = {}
        dictCD = {}
        
        for i in C:
            for j in D:
                mySum = i + j
                dictCD[mySum] = 1 if mySum not in dictCD else dictCD[mySum] + 1
        for k in A:
            for l in B:
                count = (count + dictCD[-1*(k+l)]) if -1*(k+l) in dictCD else count + 0
        
        return count