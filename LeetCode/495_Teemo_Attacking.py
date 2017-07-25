class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        tot = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] >= timeSeries[i-1] + duration:
                tot += duration
            else:
                tot += timeSeries[i] - timeSeries[i-1]
        tot += duration
        return tot

# Solution 2

    def findPoisonedDuration(self, timeSeries, duration):
        tot = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            tot -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return tot