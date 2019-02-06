class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1 or p[1] != "*":
            if len(s) == 0 or (s[0] != p[0] and p[0] != "."):
                return False
        """
        incompleted
        """
