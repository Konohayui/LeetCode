class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_rows(r, board):
            seens = []
            for i in range(9):
                digit = board[r][i]
                if digit != ".":
                    if digit in seens:
                        return False
                    seens.append(digit)
            return True
        
        def valid_cols(c, board):
            seens = []
            for i in range(9):
                digit = board[i][c]
                if digit != ".":
                    if digit in seens:
                        return False
                    seens.append(digit)
            return True
        
        def valid_cells(r, c, board):
            seens = []
            for i in range(3):
                for j in range(3):
                    digit = board[r+i][c+j]
                    if digit != ".":
                        if digit in seens:
                            return False
                        seens.append(digit)
            return True
        
        for r, c in enumerate(list(range(9))):
            if not valid_rows(r, board):
                return False
            if not valid_cols(c, board):
                return False
            
        for i in range(3):
            for j in range(3):
                if not valid_cells(i*3, j*3, board):
                    return False
                
        return True
        
        
