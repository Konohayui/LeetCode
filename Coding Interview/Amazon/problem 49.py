"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, 
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

def sum_max_subarray(array):
    if not array:
        return 0 
        
    current_max = 0 
    current_sum = 0 

    for n in array:
        current_sum = max(current_sum + n, n) 
        current_max = max(current_max, current_sum)
        
    return current_max
    
assert sum_max_subarray([34, -50, 42, 14, -5, 86]) == 137
assert sum_max_subarray([-5, -1, -8, -9]) == 0 
assert sum_max_subarray([]) == 0 
