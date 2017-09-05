class Solution(object):
    def findLHS(self, nums):
        maxCount = 0
        dic = {}
        
        for i in nums:
            lessMax = 0
            moreMax = 0
            dic[i] = 1 if i not in dic else dic[i] + 1
            if i - 1 in dic:
                lessMax += dic[i - 1]
                lessMax += dic[i]
            if i + 1 in dic:
                moreMax += dic[i + 1]
                moreMax += dic[i]
            maxCount = max(maxCount, moreMax, lessMax)
            
        return maxCount