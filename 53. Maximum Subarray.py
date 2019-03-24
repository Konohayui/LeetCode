class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        current_sum = nums[0]
        current_max = current_sum
        for n in nums[1:]:
            current_sum += n
            current_sum = max(current_sum, n)
            current_max = max(current_max, current_sum)
            
        return current_max
    
