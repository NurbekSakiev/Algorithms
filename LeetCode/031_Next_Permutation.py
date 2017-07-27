class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        start = 0
        
        if i >= 0:
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            nums[i],nums[j-1] = nums[j-1], nums[i]
            start = i + 1
        self.reverse(start, len(nums) - 1, nums)
        
    def reverse(self, start, end, nums):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1