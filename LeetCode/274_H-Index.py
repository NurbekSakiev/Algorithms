class Solution(object):
    def hIndex(self, citations):
        myArr = [0]* (len(citations) + 1)
        
        for i in citations:
            if i > len(citations):
                myArr[len(citations)] += 1
            else:
                myArr[i] += 1
                
        count = 0
        
        for j in range(len(myArr) - 1, -1, -1):
            count += myArr[j]
            if count >= j:
                return j
            
        return 0