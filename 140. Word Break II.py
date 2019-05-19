class Solution:
    def check(self, s, wordDict):
        s_len = len(s)
        dp = [False]*(s_len + 1)
        dp[0] = True
        
        for i in range(s_len):
            if dp[i]:
                for word in wordDict:
                    word_len = len(word)
                    if i+word_len <= s_len and s[i:i+word_len] == word:
                        dp[i+word_len] = True
                    
        return dp[-1]
        
    def dfs(self, s, wordDict, path, res):
        if self.check(s, wordDict):
            if not s:
                res.append(path[:-1])
                return
            
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, path + s[:i] + " ", res)
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(s) == 0 or len(wordDict) == 0:
            return []
        
        res = []
        self.dfs(s, wordDict, "", res)
        return res
    
