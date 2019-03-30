# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Apply the idea from probelm #56
"""

class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        intervals += newInterval,
        res = []
        
        for ite in sorted(intervals, key = lambda x: x.start):
            if res != [] and ite.start <= res[-1].end:
                res[-1].end = max(ite.end, res[-1].end)
            else:
                res += ite,
                
        return res
        
        
"""
new idea
"""

class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        start = newInterval.start
        end = newInterval.end
        
        right = 0
        left = 0
                
        while right < len(intervals):
            if start <= intervals[right].end:
                if end < intervals[right].start:
                    break
                
                start = min(start, intervals[right].start)
                end = max(end, intervals[right].end)
                
            else:
                left += 1
            right += 1
            
        return intervals[:left] + [Interval(start, end)] + intervals[right:]
        
