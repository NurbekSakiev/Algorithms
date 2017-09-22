class Solution(object):
    def checkSubarraySum(self, nums, k):
        dic = {0:-1}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if k != 0: 
                currSum %= k
            if currSum in dic:
                if i - dic[currSum] > 1:
                    return True
            else:
                dic[currSum] = i
        return False