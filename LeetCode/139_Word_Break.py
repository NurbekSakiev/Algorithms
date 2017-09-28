class Solution(object):
    def wordBreak(self, s, wordDict):
        if len(s) == 0:
            return True
        for i in range(1, len(s) + 1):
            word = s[:i]
            if word in wordDict and self.wordBreak(s[i:],wordDict):
                return True
        return False

# Solution 2

    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]