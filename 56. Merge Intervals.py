# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        res = []
        
        for ite in sorted(intervals, key = lambda x: x.start):
            if res != [] and ite.start <= res[-1].end:
                res[-1].end = max(ite.end, res[-1].end)
            else:
                res += [ite]
                
        return res
        
        
