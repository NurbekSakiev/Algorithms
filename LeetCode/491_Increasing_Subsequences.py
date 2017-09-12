class Solution(object):
    def findSubsequences(self, nums):
        res = set()
        self.helper([], res, nums, 0)
        return list(res)
    
    def helper(self, newList, res, nums, start):
        if len(newList) >= 2:
            res.add(tuple(newList[:]))
        for i in range(start, len(nums)):
            if len(newList) == 0 or newList[-1] <= nums[i]:
                newList.append(nums[i])
                self.helper(newList, res, nums, i + 1)
                newList.pop()