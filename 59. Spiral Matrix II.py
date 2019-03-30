class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        i = 0
        top, right, bottom, left = 0, n - 1, n - 1, 0
        
        while left <= right and top <= bottom:
            for idx in range(left, right + 1):
                i += 1
                matrix[top][idx] = i
            top += 1
            
            for idx in range(top, bottom + 1):
                i += 1
                matrix[idx][right] = i
            right -= 1
            
            for idx in range(right, left - 1, -1):
                i += 1
                matrix[bottom][idx] = i
            bottom -= 1
            
            for idx in range(bottom, top - 1, -1):
                i += 1
                matrix[idx][left] = i
            left += 1
            
        return matrix
    
