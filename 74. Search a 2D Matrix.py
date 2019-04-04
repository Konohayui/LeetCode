class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        total = rows*cols
        low, hight = 0, total
        
        while low < hight:
            mid = (low + hight)//2
            x = matrix[mid//cols][mid%cols]
            if x < target:
                low = mid + 1
            elif x > target:
                hight = mid
            else:
                return True
            
        return False

"""
simple way
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        for row in matrix:
            if target in row:
                return True
        
        return False
