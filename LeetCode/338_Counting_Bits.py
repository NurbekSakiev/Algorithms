class Solution(object):
    def countBits(self, num):
        dp = [0 for i in range(num + 1)]
        offset = 1
        for i in range(1, num + 1):
            dp[i] = dp[i / 2] + i % 2
        
        return dp