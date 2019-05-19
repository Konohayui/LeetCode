class Solution:
    def check(self, s):
        if s == s[::-1]:
            return True
        
        return False
    
    def dfs(self, s, path, res):
        if not s:
            res.append(path[:])
            return
        
        for i in range(1, len(s)+1):
            if self.check(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        
        return res
    
