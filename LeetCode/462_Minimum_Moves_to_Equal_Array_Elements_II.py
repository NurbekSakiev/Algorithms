class Solution(object):
    def minMoves2(self, nums):
        start, end = 0, len(nums) - 1
        count = 0
        while start < end:
            count += nums[end] - nums[start]
            start += 1
            end -= 1
        return count