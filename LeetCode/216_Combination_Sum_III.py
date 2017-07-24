class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        newList = []
        self.back(res, newList, k, 1, n)
        return res
    

    def back(self, res, newList, k, start, n):
        if n < 0 or k < 0:
            return
        if n == 0 and k == 0:
            res.append(newList[:])
            return res
        for i in range(start, 10):
            newList.append(i)
            self.back(res, newList, k - 1, i + 1, n - i)
            newList.pop()