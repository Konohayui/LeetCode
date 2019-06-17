class Solution:
    def helper(self, s, k, memo):
        if k == 0:
            return 1
        
        length = len(s) - k
        if s[length] == "0":
            return 0
        if memo[k] != None:
            return memo[k]
        
        ways = self.helper(s, k - 1, memo)
        if k >= 2 and int(s[length:length+2]) < 27:
            ways += self.helper(s, k - 2, memo)
        
        memo[k] = ways
        return ways
    
    def numDecodings(self, s: str) -> int:
        memo = [None]*(len(s) + 1)
        return self.helper(s, len(s), memo)
    
    
