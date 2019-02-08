class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        romans = {"CM": 900,
                  "M": 1000,
                  "CD": 400,
                  "D": 500,
                  "XC": 90,
                  "C": 100,
                  "XL": 40,
                  "L": 50,
                  "IX": 9,
                  "X": 10,
                  "IV": 4,
                  "V": 5,
                  "I": 1}
        
        num = 0
        while len(s) > 0:
            for r in romans:
                if r in s:
                    num += romans[r]
                    s = s.replace(r, "", 1)
                    
        return num
        
"""
O(n) solution
"""        

class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        romans = {"M": 1000,
                  "D": 500,
                  "C": 100,
                  "L": 50,
                  "X": 10,
                  "V": 5,
                  "I": 1}
        
        num = 0
        for i in range(len(s)-1):
            if romans[s[i]] < romans[s[i+1]]:
                num -= romans[s[i]]
            else:
                num += romans[s[i]]
            
        num += romans[s[-1]]
                    
        return num
