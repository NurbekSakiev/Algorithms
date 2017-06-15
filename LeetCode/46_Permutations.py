class Solution(object):
    def permute(self, nums):
        res = []
        newList = []
        
        self.back(res, newList, nums)
        return res
        
    def back(self, res, newList, nums):
        if len(newList) == len(nums):
            res.append(newList[:])
        else:
            for i in range(len(nums)):
                if nums[i] in newList:
                    continue
                newList.append(nums[i])
                self.back(res, newList, nums)
                newList.pop()


# Solution #2

    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms