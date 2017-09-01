class Solution(object):

    def trap(self, height):
        ans = 0
        st = []
        
        current = 0;
        
        while current < len(height):
            while len(st) > 0 and height[current] > height[st[-1]]:
                top = st.pop()
                if len(st) == 0:
                    break
                boundary = current - st[-1] - 1
                minHeight = min(height[current], height[st[-1]]) - height[top]
                ans += (boundary * minHeight)
            st.append(current)
            current += 1
        return ans

# Solution 2

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