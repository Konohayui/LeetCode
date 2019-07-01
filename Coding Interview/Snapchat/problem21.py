"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def get_classroom_num(time_intervals):
    if not time_intervals:
        return 0
        
    sorted_intervals = []
    for interval in time_intervals:
        sorted_intervals.append((interval[0], True))
        sorted_intervals.append((interval[1], False))
        
    sorted_intervals = sorted(sorted_intervals, key = lambda v: (v[0], v[1]))
    
    num, max_num = 0, 0
    for interval in sorted_intervals:
        if interval[1]:
            num += 1 
        else:
            num -= 1 
            
        max_num = max(max_num, num)
        
    return max_num 
    
