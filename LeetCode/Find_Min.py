class Solution(object):
    def findMin(self, nums):
            
        start, end = 0, len(nums) - 1
        
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = start + (end-start) / 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]
    