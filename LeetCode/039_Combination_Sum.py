class Solution(object):
    def combinationSum(self, candidates, target):
        sorted(candidates)
        res = []
        newList = []
        self.back(res, newList, 0, target, candidates)
        return res
    
    def back(self, res, newList, start, target, candidates):
        if target < 0:
            return
        elif target == 0 and newList not in res:
            res.append(newList[:])
            return
        for i in range(start, len(candidates)):
            newList.append(candidates[i])
            self.back(res, newList, i, target - candidates[i], candidates)
            newList.pop()
