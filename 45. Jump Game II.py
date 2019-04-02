class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
                
        last = len(nums) - 1
        jump, dist, max_dist = 0, 0, 0
        
        for idx, n in enumerate(nums):
            if idx > dist:
                dist = max_dist
                jump += 1
            max_dist = max(max_dist, idx + n)
            
        return jump
    
