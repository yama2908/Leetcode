class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        state = 0
        for i in range(1, len(prices)):
            state += max(prices[i] - prices[i-1], 0)
        return state
