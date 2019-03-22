class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            t = tuple(sorted(s))
            if t in res:
                res[t] += [s]
            else:
                res[t] = [s]
                
        return [sub for sub in res.values()]
        
