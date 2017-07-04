class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        newList = []
        used = [0] * len(nums)
        self.back(res, newList, nums, used)
        return res
        
    def back(self, res, newList, nums, used):
        if len(newList) == len(nums):
            res.append(newList[:])
            return
        else:
            for i in range(0, len(nums)):
                if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                newList.append(nums[i])
                self.back(res, newList, nums, used)
                used[i] = False
                newList.pop()

# Solution #2

    def permuteUnique(self, nums):
        res = [[]]
        for n in nums:
            newList = []
            for perm in res:
                for i in range(len(perm) + 1):
                    newList.append(perm[:i] + [n] + perm[i:])
                    if i < len(perm) and perm[i] == n:
                        break
            res = newList
        return res
