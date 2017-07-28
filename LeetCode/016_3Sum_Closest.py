class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = sys.maxint
        
        for i in range(len(nums) - 2):
            if i == 0 or i > 0 and nums[i] != nums[i-1]:
                low, high = i + 1, len(nums) - 1
                while low < high:
                    mySum = nums[i] + nums[low] + nums[high]
                    if abs(target - mySum) < abs(target - closest):
                        closest = mySum
                        if closest == target:
                            return closest
                    if mySum > target:
                        high -= 1
                    else:
                        low += 1
        return closest