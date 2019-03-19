class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str_to_int = {"0": 0,
                      "1": 1,
                      "2": 2,
                      "3": 3,
                      "4": 4,
                      "5": 5,
                      "6": 6,
                      "7": 7,
                      "8": 8,
                      "9": 9}
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        new_num1 = 0; new_num2 = 0
        
        for i in range(len(num1)):
            new_num1 += str_to_int[num1[i]]*(10**i)
            
        for j in range(len(num2)):
            new_num2 += str_to_int[num2[j]]*(10**j)
            
        return str(new_num1*new_num2)
        
        
