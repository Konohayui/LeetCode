class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in sorted(nums):
            res += [sub+[num] for sub in res if sub+[num] not in res]
            
        return res
    
