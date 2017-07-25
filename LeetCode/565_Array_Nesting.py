class Solution(object):
    def arrayNesting(self, nums):
        maxSize = 0
        
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            size = 0
            idx = nums[i]
            while nums[idx] >= 0:
                temp = nums[idx]
                nums[idx] = -1
                idx = temp
                size += 1
            maxSize = max(maxSize, size)
        return maxSize