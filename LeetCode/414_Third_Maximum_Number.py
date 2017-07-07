class Solution(object):
    def thirdMax(self, nums):
        first, second, third = None, None, None
        
        for i in nums:
            if first == None or second == None or third == None:
                if first == None:
                    first = i
                elif second == None and i != first:
                    second = i
                elif third == None and i != first and i != second:
                    third = i
            elif i > first:
                third = second
                second = first
                first = i
            elif i > second:
                third = second
                second = i
            elif i > third:
                third = i
        print first, second, third
        if third == None:
            if second != None:
                return second
            return first
        return third
                
        """
        :type nums: List[int]
        :rtype: int
        """