class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_position(nums: List[int], target: int, left = True) -> int:
            l = 0
            r = len(nums)
            
            while l < r:
                mid = (l + r)//2
                if nums[mid] == target:
                    if left:
                        r = mid
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
                    
            return l
        
        if not nums:
            return [-1, -1]
        
        left = search_position(nums, target, left = True)
        right = search_position(nums, target, left = False)
        
        # if left == right:
        #     return [left, right]
        if 0 <= left < len(nums) and nums[left] == target:
            return [left, right - 1]
        else: 
            return [-1, -1]
