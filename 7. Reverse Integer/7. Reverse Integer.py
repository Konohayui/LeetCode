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
