"""
As test sample size is small, 
time complexities of these two approaches
are closed.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        total_nums = len(nums)
        
        for idx in range(total_nums):
            if nums[idx] > target or nums[idx] == target:
                return idx
        return total_nums
        
        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
