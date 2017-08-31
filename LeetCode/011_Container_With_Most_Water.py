class Solution(object):
    def maxArea(self, height):
        maxVol = float("-inf")
        start, end = 0, len(height) - 1
        
        while start < end:
            maxVol = max(maxVol, (end - start) * (min(height[start], height[end])))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxVol