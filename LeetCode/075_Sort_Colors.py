class Solution(object):
    def sortColors(self, nums):
        twos,zeros = len(nums) - 1,  0
        i = 0
        while i<= twos:
            while nums[i] == 2 and i < twos:
                nums[i], nums[twos] = nums[twos], nums[i]
                twos -= 1
            while nums[i] == 0 and i > zeros:
                nums[i], nums[zeros] = nums[zeros], nums[i]
                zeros += 1
            i += 1
