class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        elif len(set(s)) == 1:
            return s
        elif len(set(s)) == len(s):
            return s[0]
        
        else:
            longest_len = 0
            longest_pal = ""
            
            for head_idx in range(len(s)):
                for end_idx in range(head_idx, len(s)):
                    sub_str = s[head_idx:end_idx+1]
                    if sub_str == sub_str[::-1]:
                        if len(sub_str) >= longest_len:
                            longest_pal = sub_str
                            longest_len = len(sub_str)

            return longest_pal
            
            
            
"""
better solution:
search from center
"""

class Solution:
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            temp = self.helper(s, i, i) # case cabad, odd
            if len(temp) > len(res):
                res = temp
                
            temp = self.helper(s, i, i+1) # case cabbad, even
            if len(temp) > len(res):
                res = temp
                
        return res
        
    
