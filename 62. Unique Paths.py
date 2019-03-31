"""
the robot takes (m+n-2) steps to reach the star,
and it always take m-1 right steps;
thus, the robot has C(m+n-2, m-1) ways to step
right or C(m+n-2, n-1) to step down.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m and not n:
            return 0
        
        grid = [1]*n
        
        for i in range(1, m):
            for j in range(1, n):
                grid[j] += grid[j-1]
        
        return grid[-1]
    
