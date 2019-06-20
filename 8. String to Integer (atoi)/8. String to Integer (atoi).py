class Solution:
    def myAtoi(self, str: 'str') -> 'int':
        if not str:
            return 0
        
        str = str.strip() # remve whitespaces
        if len(str) < 1:
            return 0
        
        sign = 1
        idx = 0
        if str[0] == "-":
            sign = -1
            idx = 1
        elif str[0] == "+":
            sign = sign
            idx = 1
        
        num = 0
        for n in str[idx:]:
            if n not in "1234567890":
                break
            num = 10*num + ord(n) - ord("0")

        num = sign*int(num)
        if num > 2**31 - 1:
            return 2**31 - 1
        elif num < -2**31:
            return -2**31
        return num
        
            
"""
better solution
"""
class Solution:
    def myAtoi(self, s: 'str') -> 'int':
        if not str:
            return 0
        
        s = s.strip()
        if len(s) == 0:
            return 0
        
        sign = 1
        idx = 0
        if s[0] == "-":
            sign = -1
            idx = 1
        elif s[0] == "+":
            sign = sign
            idx = 1
        
        res = ""
        for n in s[idx:]:
            if n.isdigit():
                res += n
            else:
                break
                
        num = sign*int(res) if len(res) != 0 else 0
        if num > 2**31 - 1:
            return 2**31 - 1
        elif num < -2**31:
            return -2**31
        return num
        
