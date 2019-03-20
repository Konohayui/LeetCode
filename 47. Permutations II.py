"""
follow combination sumII
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res, temp, l):
            if len(temp) == l:
                res += [temp]
                return
            
            for i in range(len(nums)):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], res, temp + [nums[i]], l)
        
        l = len(nums)
        res = []
        nums.sort()
        backtrack(nums, res, [], l)
        
        return res
    
    
