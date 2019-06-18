class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(set(s)) < 2:
            return len(set(s))
        
        str_len = len(s)
        longest_sub_len = 0
        
        for i in range(str_len):
            sub_str = []
            for j in range(i, str_len):
                if s[j] in sub_str:
                    break
                sub_str.append(s[j])
            longest_sub_len = max(longest_sub_len, len(sub_str))
        return longest_sub_len
        
"""
Better solution
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(set(s)) < 2:
            return len(set(s))
        
        longest_sub_len = 0
        sub_str = ""
        for letter in s:
            if letter not in sub_str:
                sub_str += letter
            else:
                longest_sub_len = max(longest_sub_len, len(sub_str))
                sub_str = sub_str[sub_str.index(letter) + 1:]
                sub_str += letter
            longest_sub_len = max(longest_sub_len, len(sub_str))
        return longest_sub_len
    
    
"""
much better solution
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used_char = {}
        maxlen = 0
        start = 0
        
        for i, c in enumerate(s):
            if c in used_char and used_char[c] >= start:
                start = used_char[c] + 1
            used_char[c] = i
            maxlen = max(i - start + 1, maxlen)
        return maxlen
        
