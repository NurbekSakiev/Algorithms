class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, len(s) + 1):
            if self.isValid(s[i-1:i]):
                dp[i] += dp[i-1]
            if self.isValid(s[i-2:i]):
                dp[i] += dp[i-2]
        return dp[-1]
    
    
    def isValid (self, s):
        if s[0] == "0":
            return False
        num = int(s)
        if 1 <= num <= 26:
            return True