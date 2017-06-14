class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        newList = []
        self.back(res, 0, newList, target, candidates)
        return res
        
    def back(self, res, start, newList, target, candidates):
        if target < 0:
            return
        if target == 0:
            if newList not in res:
                res.append(newList[:])
            return 
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            newList.append(candidates[i])
            self.back(res, i + 1, newList, target - candidates[i], candidates)
            newList.pop()