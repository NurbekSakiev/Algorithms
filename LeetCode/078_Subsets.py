class Solution(object):
    def subsets(self, nums):
        res = []
        newList = []
        self.back(res, newList, nums, 0, len(nums))
        return res
        
    def back(self, res, newList, nums, start, end):
        if newList not in res:
            res.append(newList[:])
        for i in range(start,end):
            newList.append(nums[i])
            self.back(res, newList, nums, i+1, end)
            newList.pop()