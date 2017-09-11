class Solution(object):
    def canPartition(self, nums):
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        tot /= 2
        
        dp = [[False for i in range(tot + 1)] for j in range(len(nums) + 1)]
        
        dp[0][0] = True
        
        for i in range(1, len(nums) + 1):
            dp[i][0] = True
            for j in range(1, tot + 1):
                dp[0][j] = False
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[len(nums)][tot]

# Solution 2

    def canPartition(self, nums):
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        tot /= 2
        
        dp = [False for i in range(tot + 1)]
        
        dp[0] = True
        
        for num in nums:
            for i in range(tot, 0, -1):
                if i >= num:
                    dp[i] = dp[i] or dp[i-num]
                print dp
        return dp[tot]