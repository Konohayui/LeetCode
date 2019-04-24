class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        
        triangle = [[1]*(r+1) for r in range(numRows)]
        for r in range(numRows):            
            for c in range(1, r):
                triangle[r][c] = triangle[r-1][c-1] + triangle[r-1][c]
            
        return triangle
    
