"""
simple solution
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
            

"""
cycle detection
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        meet = slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while meet != slow:
                    meet = nums[meet]
                    slow = nums[slow]
                    
                return meet
            
            
