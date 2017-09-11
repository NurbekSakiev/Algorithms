class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        first = sys.maxint
        second = sys.maxint
        
        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False