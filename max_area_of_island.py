class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        mvs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                
                stack = [[i, j]]
                grid[i][j] -= 1
                shape = 0
                while stack:
                    pos = stack.pop()
                    shape += 1
                    for mv in mvs:
                        try:
                            x = pos[0] + mv[0]
                            y = pos[1] + mv[1]
                            if x >= 0 and y >= 0 and grid[x][y] == 1:
                                stack.append([x, y])
                                grid[x][y] -= 1
                        except:
                            pass
                ans = max(ans, shape)
        return ans
