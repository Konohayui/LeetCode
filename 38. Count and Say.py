class Solution:
    def countAndSay(self, n: int) -> str:
        it = 1
        string = "1"
        
        while it < n:
            count = 1
            new_string = ""
            
            for i in range(len(string)):
                if i == len(string) - 1:
                    new_string += str(count) + string[i]
                elif string[i] == string[i+1]:
                    count += 1
                else:
                    new_string += str(count) + string[i]
                    count = 1
                    
            string = new_string
            it += 1
            
        return string
            
