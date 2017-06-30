class Solution(object):
    def singleNumber(self, nums):
        myNum = 0
        for i in nums:
            myNum ^= i
        return myNum