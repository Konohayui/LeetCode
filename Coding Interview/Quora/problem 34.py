"""
Given a string, find the palindrome that can be made by inserting 
the fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be made, 
return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", 
since we can add three letters to it (which is the smallest amount to make a palindrome). 
There are seven other palindromes that can be made from "race" by adding three letters, 
but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

def min_insertion_pal(s):
    if s == s[::-1]:
        return s
        
    if s[0] == s[-1]:
        return s[0] + min_insertion_pal(s[1:-1]) + s[0]
    else:
        str1 = s[0] + min_insertion_pal(s[1:]) + s[0]
        str2 = s[-1] + min_insertion_pal(s[:-1]) + s[-1]
        
        if len(str1) < len(str2):
            return str1
        elif len(str1) > len(str2):
            return str2 
        else:
            return str1 if str1 < str2 else str2
            
assert min_insertion_pal("race") == "ecarace"
assert min_insertion_pal("google") == "elgoogle"
assert min_insertion_pal("banana") == "bananab"
assert min_insertion_pal("ace") == "acea"

