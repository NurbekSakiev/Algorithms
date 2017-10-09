class Solution(object):

    def longestPalindromeSubseq(self, s):
        return self.helper(s, 0, len(s))
    
    
    def helper(self, s, start, l):
        if l == 0:
            return 0
        if l == 1:
            return 1
        if s[start] == s[start + l - 1]:
            return 2 + self.helper(s, start + 1, l - 2)
        else:
            return max(self.helper(s, start + 1, l- 1), self.helper(s, start, l - 1))

# Solution 2 DP

    def longestPalindromeSubseq(self, s):
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i + 1][j])
        
        return dp[0][-1]

# Solution 3

    def longestPalindromeSubseq(self, s):
  
        curr = [0 for i in range(len(s))]
        prev = [0 for i in range(len(s))]
        
        for i in range(len(s) - 1, -1, -1):
            curr[i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    curr[j] = prev[j - 1] + 2
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr[:]
        return prev[-1]