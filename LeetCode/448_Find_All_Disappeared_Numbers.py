class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        
        for j in range(len(nums)):
            if nums[j] > 0:
                res.append(j + 1)
        return res