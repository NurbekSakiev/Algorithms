class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        res = []
        st = []
        d = {}
        
        for n in nums:
            while len(st) and st[-1] < n:
                d[st.pop()] = n
            st.append(n)
        for f in findNums:
            res.append(d.get(f, -1))
        return res