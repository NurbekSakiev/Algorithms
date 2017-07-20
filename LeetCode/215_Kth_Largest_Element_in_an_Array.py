class Solution(object):
    def findKthLargest(self, nums, k):
        
        randNum = nums[len(nums) - k - 1]
        nums1, nums2, nums3 = [],[],[]
        
        for i in nums:
            if i < randNum:
                nums1.append(i)
            elif i == randNum:
                nums2.append(i)
            else:
                nums3.append(i)
            
        if k <= len(nums3):
            return self.findKthLargest(nums3, k)
        elif len(nums3) + len(nums2) < k:
            return self.findKthLargest(nums1, k - (len(nums3) + len(nums2)))
        else:
            return nums2[0]