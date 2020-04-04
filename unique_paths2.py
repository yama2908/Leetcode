class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * c
        dp[0] = 1 - obstacleGrid[0][0]
        for i in range(1, c):
            dp[i] = dp[i-1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            dp[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, c):
                dp[j] += dp[j-1]
                dp[j] *= (1 - obstacleGrid[i][j])
        return dp[-1]
