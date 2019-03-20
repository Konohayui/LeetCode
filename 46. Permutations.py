class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res, temp, l):
            if len(temp) == l:
                res += [temp]
                return
            
            for n in nums:
                if n in temp:
                    continue

                backtrack(nums, res, temp + [n], l)
            
        l = len(nums)
        res = []
        backtrack(nums, res, [], l)
        
        return res
        
        
