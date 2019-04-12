"""
f(n) = f(0)f(n-1) + f(1)(n-2) + ... + f(n-2)f(1) + f(n-1)f(0)
"""

class Solution:
    def numTrees(self, n: int) -> int:
        res = [0]*(n+1)
        res[0] = 1
        res[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                res[i] += res[i-j]*res[j-1] # right node nums x left node nums 
                
        return res[-1]
    
    
