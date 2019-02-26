class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        else:
            for idx in range(nums_len-1, 0, -1):
                if nums[idx] == nums[idx-1]:
                    nums.pop(idx)
            return len(nums)
