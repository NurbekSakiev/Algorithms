class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        newList = []
        self.permutation(res, nums, 0)
        return res
    

    def permutation(self, res, nums, start):
        if start >= len(nums) and nums not in res:
            res.append(nums[:])
        else:
            for i in range(start, len(nums)):
                if start != i and nums[i] == nums[start]:
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                self.permutation(res, nums, start + 1)
                nums[start], nums[i] = nums[i], nums[start]