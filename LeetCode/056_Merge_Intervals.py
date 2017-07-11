# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):

    def merge(self, intervals):
        
        out = []
        
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out.append(i)
            
        return out

    # Solution #2

    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
            
        intervals = sorted(intervals)
        start = intervals[0].start
        end = intervals[0].end
        res = []
        
        for i in intervals:
            if end >= i.start:
                end = max(end, i.end)
            else:
                res.append(Interval(start, end))
                start, end = i.start, i.end
            
        res.append(Interval(start, end))
        return res
