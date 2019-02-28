class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
#         while dividend >= divisor:
#             dividend -= divisor
#             res += 1
            
    
        quotient = 0
        for i in range(31, -1, -1): 
            if (res + (divisor << i) <= dividend): 
                res += divisor << i
                quotient |= 1 << i
                
        if not positive:
            quotient = -quotient
        return min(max(-2147483648, quotient), 2147483647)
        
                
        
