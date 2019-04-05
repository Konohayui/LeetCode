class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        
        res = []
        self.dfs(n, 1, k, [], res)
        return res
    
    def dfs(self, n, idx, k, path, res):
        if k == 0:
            res += path,
            return
            
        for i in range(idx, n+1):
            self.dfs(n, i + 1, k - 1, path + [i], res)
            
