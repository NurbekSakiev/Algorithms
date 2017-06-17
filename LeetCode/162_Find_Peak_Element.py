class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) < 1:
            return -1
            
        high, low = len(nums) - 1, 0
        
        while low < high:
            mid = (high + low) / 2
            mid2 = mid + 1
            if nums[mid] < nums[mid2]:
                low = mid2
            else:
                high = mid
        return low