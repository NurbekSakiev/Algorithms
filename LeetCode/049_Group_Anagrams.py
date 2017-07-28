class Solution(object):
    def groupAnagrams(self, strs):
        myDict = {}
        res = []
        
        for i in strs:
            ana = ''.join(sorted(i))
            if ana in myDict:
                myDict[ana].append(i)
            else:
                myDict[ana] = [i]
            
        for k,v in myDict.items():
            res.append(v)
        
        return res