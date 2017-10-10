class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = [1 for i in range(len(pairs))]
        
        for i in range(1, len(pairs)):
            curr = 1
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(curr, dp[j] + 1)
                    curr = max(curr, dp[i])
        return dp[-1]


    def findLongestChain(self, pairs):
        curr, res = float('-inf'), 0
        for p in sorted(pairs, key = lambda x: x[1]):
            if curr < p[0]:
                curr = p[1]
                res = res + 1
        return res