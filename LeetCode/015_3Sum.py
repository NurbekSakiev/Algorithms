class Solution(object):
    def threeSum(self, nums):
        res = []
        
        nums.sort()
        print nums
        for i in range(len(nums)-2):
            if i == 0 or (i > 0 and  nums[i] != nums[i-1]):
                low, high, mySum = i + 1, len(nums) - 1, 0 - nums[i]
                while low < high:
                    if(nums[low] + nums[high] == mySum):
                        res.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < mySum:
                        low += 1
                    else:
                        high -= 1
        return res