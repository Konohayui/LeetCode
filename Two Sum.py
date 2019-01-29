class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        combs = {}
        for idx, n in enumerate(nums):
            r = target - n
            if r in combs:
                return combs[r], idx
            combs[n] = idx
