class Solution:
    def dfs(self, nums: List[int], idx: int, path: List[int], res: List[List[int]]):
        res += path,
        for i in range(idx, len(nums)):
            self.dfs(nums, i+1, path + [nums[i]], res)
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        
        return res
    
