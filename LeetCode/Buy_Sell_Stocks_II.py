class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 1:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i+1] - prices[i]
        return profit