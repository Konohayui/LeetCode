class Solution:
    def helper(self, curr: 'str', res: 'List', n: 'int', left: 'int', right: 'int'):
        if right == n:
            res.append(curr)
        if left < n:
            self.helper(curr+"(", res, n, left+1, right)
        if right < left:
            self.helper(curr+")", res, n, left, right+1)
        
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0:
            return []
        
        res = []
        self.helper("", res, n, 0, 0)
        return res
