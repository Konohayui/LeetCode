"""
You are given an array of non-negative integers that represents a 
two-dimensional elevation map where each element is unit-width wall 
and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
"""

def trap(heights):
    if not heights or len(heights) < 3:
           return 0
        
    volume = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
        
    while left < right:
        left_max, right_max = max(left_max, heights[left]), max(right_max, heights[right])
        if left_max <= right_max:
            volume += left_max - heights[left]
            left += 1
        else:
            volume += right_max - heights[right]
            right -= 1
        
    return volume
    
assert trap([2,1,2]) == 1 
assert trap([3, 0, 1, 3, 0, 5]) == 8

    
