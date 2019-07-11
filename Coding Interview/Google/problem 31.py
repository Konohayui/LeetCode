"""
The edit distance between two strings refers to the minimum number of character 
insertions, deletions, and substitutions 
required to change one string to the other. 
For example, the edit distance between 
“kitten” and “sitting” is three: substitute the 
“k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, n+1):
        dp[0][i] = i 
        
    for j in range(1, m+1):
        dp[j][0] = j 
        
    for r in range(1, m+1):
        for c in range(1, n+1):
            if str1[r-1] == str2[c-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1 
                
    return dp[-1][-1]
    
assert(edit_distance("kitten", "sitting") == 3)
assert(edit_distance("hello", "hi") == 4)
assert(edit_distance("", "") == 0)



