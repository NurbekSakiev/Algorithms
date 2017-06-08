class NumArray(object):

    def __init__(self, nums):
        if len(nums) == 0:
            return None
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.res = nums
        """
        :type nums: List[int]
        """
        

    def sumRange(self, i, j):
        if i == 0:
            return self.res[j]
        else:
            return self.res[j] - self.res[i - 1]