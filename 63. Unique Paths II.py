class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [1] + [0]*(n - 1)
            
        for i in range(1, n):
            res[i] = res[i-1]*(1 - obstacleGrid[0][i])
            
        for i in range(1, m):
            res[0] *= 1 - obstacleGrid[i][0]
            for j in range(1, n):
                res[j] = (res[j] + res[j-1])*(1 - obstacleGrid[i][j])
                
        return res[-1]
        
