class Solution(object):
    def kEmptySlots(self, flowers, k):
        active = []
        for day, flower in enumerate(flowers, 1):
            idx = bisect.bisect(active, flower)
            for neighbor in active[idx - (idx > 0): idx + 1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(idx, flower)
        return -1