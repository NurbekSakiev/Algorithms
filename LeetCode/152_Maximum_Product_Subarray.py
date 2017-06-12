class Solution(object):
    
    def maxProduct(self, nums):
        if len(nums) < 1:
            return 0
        maxSoFar, minPreHere, maxPreHere = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            maxHere = max(maxPreHere * nums[i], minPreHere * nums[i], nums[i])
            minHere = min(maxPreHere * nums[i], minPreHere * nums[i], nums[i])
            maxSoFar = max(maxHere, maxSoFar)
            maxPreHere = maxHere
            minPreHere = minHere
        
        return maxSoFar

#Solution #2
    def maxProduct(self, nums):
        if len(nums) < 1:
            return 0
        imax, imin, maxSoFar = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
                
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            maxSoFar = max(imax, maxSoFar)
        
        return maxSoFar


    