class Solution(object):
    def minSubArrayLen(self, s, nums):
        res = sys.maxint
        left, right = 0, 0
        currSum = 0
        while right < len(nums):
            currSum += nums[right]
            while currSum >= s:
                res = min(res, right - left + 1)
                currSum -= nums[left]
                left += 1
            right += 1
        return res if res != sys.maxint else 0
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        