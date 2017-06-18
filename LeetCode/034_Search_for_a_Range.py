class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1,-1]
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if nums[low] != target:
            return [-1,-1]
        left = low
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) / 2 + 1
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid
            
        return [left, high]