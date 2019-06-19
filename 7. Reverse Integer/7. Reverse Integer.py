class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        x = str(x)
        
        if x[0] != "-":
            x = int(x[::-1])
        else:
            sign = x[0]
            x = x[1:][::-1]
            x = sign + x
            x = int(x)
            
        if -2**31 <= x <= 2**31-1:
            return x
        return 0

"""
better solution
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        threshold = 2**31
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            carried = x%10
            x //= 10
            
            if (sign*res > threshold/10) or (sign*res == threshold/10 and carried > 7):
                return 0
            elif (sign*res < -threshold/10) or (sign*res == -threshold/10 and carried < -8):
                return 0
            res = res*10 + carried

        return sign*res
        
        
