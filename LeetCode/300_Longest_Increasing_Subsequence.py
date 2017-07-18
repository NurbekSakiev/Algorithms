class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        fin = [1 for i in range(len(nums))]
      
        
        for i in range(len(nums)):
            greatest = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    greatest = max(greatest, fin[j])
            fin[i] = greatest + 1
     
        return max(fin)