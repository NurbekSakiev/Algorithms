class Solution(object):
    def summaryRanges(self, nums):
        
        res = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))
            i += 1
        return res