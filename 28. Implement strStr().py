class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            head = needle[0]
            idx = 0
            
            for s in haystack:
                if head == s:
                    if haystack[idx:idx + len(needle)] == needle:
                        return idx
                idx += 1
            
        return -1
