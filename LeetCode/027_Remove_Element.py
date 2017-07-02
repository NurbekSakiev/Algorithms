class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in nums:
            if j != val:
                nums[i] = j
                i += 1
        return i