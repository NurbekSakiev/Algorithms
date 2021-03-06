# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        
        i = 0
        
        while i < len(intervals) and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval = Interval(min(intervals[i].start, newInterval.start), max(intervals[i].end, newInterval.end))
            i += 1
        res.append(newInterval)
        while i < len(intervals):
            res.append(intervals[i])
            i +=1
        return res