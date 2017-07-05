class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxSoFar = 0
        maxTot = 0
        consec = True
        
        
        for i in range(len(nums)):
            if nums[i] == 1:
                maxSoFar += 1
                maxTot = max(maxTot, maxSoFar)
            else:
                maxSoFar = 0
        return maxTot