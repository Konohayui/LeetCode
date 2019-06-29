class Solution:
    digs_to_letts = {"1": "*",
                     "2": "abc",
                     "3": "def",
                     "4": "ghi",
                     "5": "jkl",
                     "6": "mno",
                     "7": "pqrs",
                     "8": "tuv",
                     "9": "wxyz"}
    
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        
        num_len = len(digits)
        if num_len == 0 or not digits:
            return []
        
        if num_len == 1:
            return list(self.digs_to_letts[digits])
        else:
            result = []
            for l in self.digs_to_letts[digits[0]]:
                result += [l+letters for letters in self.letterCombinations(digits[1:])]
            return result
        
