"""
n = 1, 1
n = 2, 2
n = 3, 3
n = 4, 5
n = 5, 8
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
            
        return a
    
