class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white = 0, 0
        
        for idx in range(len(nums)):
            color = nums[idx]
            nums[idx] = 2
            
            if color < 2:
                nums[white] = 1
                white += 1
                
            if color == 0:
                nums[red] = 0
                red += 1
                
                
