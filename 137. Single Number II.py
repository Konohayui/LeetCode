class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0; two = 0; three = 0
        
        for i in range(len(nums)):
            two |= nums[i] & one
            one = nums[i] ^ one
            three = ~(one & two)
            one &= three
            two &= three
            
        return one
    
