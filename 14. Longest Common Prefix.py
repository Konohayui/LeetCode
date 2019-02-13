class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        else:
            
            strs = sorted(strs, key = len)
            prefix = ""
            res = ""
            for i in range(len(strs[0])):
                prefix += strs[0][i]
                for word in strs[1:]:
                    if prefix not in word[:i+1]:
                        return res
                    
                res = prefix
            return res
