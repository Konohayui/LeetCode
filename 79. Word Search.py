class Solution:
    def dfs(self, board: List[List[str]], di: int, dj: int, word: str) -> bool:
        if word[0] == board[di][dj]:
            if len(word[1:]) == 0:
                return True
        
            board[di][dj] = "-"
            if di > 0 and self.dfs(board, di-1, dj, word[1:]): # up
                return True
            if di < len(board)-1 and self.dfs(board, di+1, dj, word[1:]): # down
                return True
            if dj > 0 and self.dfs(board, di, dj-1, word[1:]): # left
                return True
            if dj < len(board[0])-1 and self.dfs(board, di, dj+1, word[1:]): # right
                return True
            board[di][dj] = word[0]
            
        else:
            return False
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if self.dfs(board, r, c, word):
                    return True
                
        return False
    
    
