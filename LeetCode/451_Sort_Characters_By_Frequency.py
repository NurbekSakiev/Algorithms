class Solution(object):
    def frequencySort(self, s):
        res=""
        arr = [0] * len(s)
        myDict = {}
        
        for i in s:
            myDict[i] = 1 if i not in myDict else myDict[i] + 1
        
        for k,v in myDict.items():
            if arr[v-1] == 0:
                arr[v-1] = [k]
            else:
                arr[v-1].append(k)
        
        for j in range(len(arr) - 1, -1, -1):
            if arr[j] != 0:
                for k in range(len(arr[j])):
                    res += (arr[j][k] * (j+1))
        return res
        
        """
        :type s: str
        :rtype: str
        """
        