class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2 = 0,0
        num1, num2 = 0,1
        
        for i in nums:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
            elif count1 == 0:
                num1 = i
                count1 = 1
            elif count2 == 0:
                num2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        return [n for n in (num1, num2) if nums.count(n) > len(nums) // 3]