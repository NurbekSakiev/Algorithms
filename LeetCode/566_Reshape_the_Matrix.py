class Solution(object):
    def matrixReshape(self, nums, r, c):
        
        if len(nums) == 0  or len(nums[0]) == 0:
            return nums
        
        l, w = len(nums), len(nums[0])
        
        if l * w != r * c:
            return nums
        
        res = [[None for i in range(c)] for j in range(r)]
        count = 0
        
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                res[count / c][count % c] = nums[i][j]
                count += 1
        
        return res