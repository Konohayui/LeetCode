class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0 or len(wordDict) == 0:
            return False
        
        string_length = len(s)
        dp = [False]*(string_length + 1)
        dp[0] = True
        
        for i in range(string_length):
            if dp[i]:
                for word in wordDict:
                    j = len(word)
                    if i+j <= string_length and s[i:i+j] == word:
                        dp[i+j] = True
                        
        return dp[-1]
    
    
