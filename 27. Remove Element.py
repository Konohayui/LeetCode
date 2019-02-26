class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        
        count = 0
        for idx in range(nums_len):
            if nums[idx] != val:
                nums[count], nums[idx] = nums[idx], nums[count]
                count += 1
        return count
