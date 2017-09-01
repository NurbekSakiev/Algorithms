class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        tot = 0
        leftMax, rightMax = 0, 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    tot += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    tot += rightMax - height[right]
                right -= 1
        return tot