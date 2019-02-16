class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if len(s) == 0:
            return True
        else:
            seens = []
            closed_parentheses = {")": "(", "]": "[", "}": "{"}
            
            for p in s:
                if p in closed_parentheses:
                    if len(seens) > 0 and seens[-1] == closed_parentheses[p]:
                        seens.pop()
                    else:
                        return False
                else:    
                    seens.append(p)
                
            return seens == []
                
