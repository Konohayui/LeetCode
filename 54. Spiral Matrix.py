class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        spiral = []
        while matrix and matrix[0]:
            spiral.extend(matrix.pop(0))
            
            if matrix and matrix[0]:
                for row in matrix:
                    spiral.append(row.pop())
                    
            if matrix:
                spiral.extend(matrix.pop()[::-1])
                
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    spiral.append(row.pop(0))
                    
        return spiral
    
    
