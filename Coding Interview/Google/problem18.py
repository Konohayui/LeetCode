"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

* 10 = max(10, 5, 2)
* 7 = max(5, 2, 7)
* 8 = max(2, 7, 8)
* 8 = max(7, 8, 7)
"""

"""
O(n)
double-ended queue
"""

def find_max(array):
  # windows will record elements' indexes
  res, windows = [], []
  
  for i, n in enumerate(array):
    # keep/make sure the rightmost element is the smallest
    while windows and array[windows[-1]] <= n:
      windows.pop()
    
    # add new element
    windows.append(i)
    
    # once the size of windows is larger 
    # than k, remove the leftmost element
    if i - windows[0] >= k:
      windows.pop(0)
    
    # add the maximum element in the windows
    if i + 1 >= k:
      res.append(array[windows[0]])
      
  return res
  
  
