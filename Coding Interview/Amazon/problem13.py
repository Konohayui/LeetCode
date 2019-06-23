"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

"""
brute force
O(n^3)
"""
def subarraysWithKDistinct(nums, k):
    max_len = 0
    res = ""
    length = len(nums)
    for i in range(length):
        for j in range(i, length):
            temp = nums[i:j+1]
            if len(set(temp)) == k and len(temp) > max_len:
                res = temp
                max_len = len(res)
                    
    return res
    
print(subarraysWithKDistinct([1, 2, 1, 2, 3], 2))

