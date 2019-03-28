class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        goal = len(nums) - 1
        dis = 0
        for pos, num in enumerate(nums):
            if pos > dis:
                return False
            if dis == goal:
                return True
            dis = max(dis, pos + num)
            
        return True
    
    
