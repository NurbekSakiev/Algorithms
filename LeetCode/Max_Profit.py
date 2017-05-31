class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        currMin = sys.maxint
        
        for i in range(len(prices)):
            currMin = min(currMin, prices[i])
            maxProfit = max(prices[i] - currMin, maxProfit)
        return maxProfit