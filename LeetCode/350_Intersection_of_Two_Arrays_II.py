class Solution(object):
    def intersect(self, nums1, nums2):
        myDict = {}
        res = []
        
        for i in nums1:
            myDict[i] = myDict[i] + 1 if i in myDict else 1
        
        for j in nums2:
            if j in myDict and myDict[j] > 0:
                res.append(j)
                myDict[j] -= 1
        
        return res