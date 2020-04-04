class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)
        
