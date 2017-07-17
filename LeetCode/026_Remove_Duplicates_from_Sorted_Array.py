class Solution(object):
    def removeDuplicates(self, nums):
        i, j = 1, 1
        if len(nums) < 2:
            return len(nums)
        
        while j < len(nums):
            if j < len(nums) and nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        nums = nums[:i+1]
        return i