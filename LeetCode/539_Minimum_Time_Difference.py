class Solution(object):
    def findMinDifference(self, timePoints):
        mark = [0] * 24 * 60
        
        for time in timePoints:
            t = time.split(":")
            h = int(t[0])
            m = int(t[1])
            
            if mark[h * 60 + m]:
                return 0
            mark[h * 60 + m] = 1
        
        first = sys.maxint
        last = float("-inf")
        minT = sys.maxint
        for i in range(24*60):
            if mark[i]:
                if (first != sys.maxint):
                    minT = min(minT, i - prev)
                first = min(first, i)
                last = max(last, i)
                prev = i
        minT = min(minT, (24*60 - last + first))
        return minT