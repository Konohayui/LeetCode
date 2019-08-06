"""
Given a list of integers S and a target number k, 
write a function that returns a subset of S that adds up to k. 
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

def get_subset_sum(s, k):
    if len(s) == 0:
        return None
    
    if s[0] == k:
        return [s[0]]
        
    has_element = get_subset_sum(s[1:], k - s[0])
    if has_element:
        return [s[0]] + has_element
    else:
        return get_subset_sum(s[1:], k)
        
assert get_subset_sum([1, 2, 3], 4) == [1, 3]
assert get_subset_sum([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]
assert get_subset_sum([100, 3, 5], 1) == None
assert get_subset_sum([-12, 15, 3], -9) == [-12, 3]

