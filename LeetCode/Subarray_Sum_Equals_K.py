# Subarray Sum Equals K
# LeetCode

class Solution(object):
    def subarraySum(self, nums, k):
        
        res = 0
        myDict = {0:1}
        mySum = 0
        for i in range(len(nums)):
            mySum += nums[i]
            res += myDict.get(mySum - k, 0)
            myDict[mySum] = myDict.get(mySum, 0) + 1
        return res