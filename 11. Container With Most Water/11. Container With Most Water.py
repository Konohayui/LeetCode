class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        if len(height) == 0:
            return 0
        elif len(height) == 2:
            return min(height)
        else:
            max_area = 0
            left = 0; right = len(height)-1
            
            while left < right:
                w = right - left
                h = min(height[left], height[right])
                max_area = max(w*h, max_area)
                
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
                    
            return max_area
        
        
