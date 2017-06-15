class Solution(object):
    def findDuplicate(self, nums):
        if not nums:
            return -1
            
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

Solution #2

class Solution(object):
    def findDuplicate(self, nums):
        low, high = 1, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) / 2
            count = 0
            
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low

