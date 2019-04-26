class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        depth = len(triangle)
        for d in range(depth-1, 0, -1):
            for i in range(d):
                triangle[d-1][i] = min(triangle[d][i]+triangle[d-1][i],
                                       triangle[d][i+1]+triangle[d-1][i])
                
        return triangle[0][0]
    
    
