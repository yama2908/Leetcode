class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1] + prices[i] - prices[i-1], 0)
        return max(dp)
