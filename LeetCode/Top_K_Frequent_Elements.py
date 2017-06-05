# Top K Frequent Elements
# LeetCode

class Solution(object):
    def topKFrequent(self, nums, k):
        
        myArr = [None] * (len(nums) + 1)
        myDict = {}
        res = []
        for i in nums:
            myDict[i] = 1 if i not in myDict else myDict[i] + 1
        
        for key,v in myDict.items():
            if myArr[v] == None:
                myArr[v] = [key]
            else:
                myArr[v].append(key)
            
        for j in range(len(nums), -1, -1):
            if myArr[j] != None and k != 0:
                for l in range(len(myArr[j])):
                    if k == 0:
                        return res
                    res.append(myArr[j][l])
                    k -= 1
        return res
        