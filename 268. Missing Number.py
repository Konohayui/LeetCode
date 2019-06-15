class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        expected_sum = (n*(n - 1))//2
        given_sum = sum(nums)
            
        return expected_sum - given_sum
    
    
