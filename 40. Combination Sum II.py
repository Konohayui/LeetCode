class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def depth_first_search(candidates, target, temp_sol, sols):            
            if target == 0:
                sols += [temp_sol]
                
                return
        
            for i in range(len(candidates)):
                if candidates[i] == candidates[i-1] and i != 0:
                    continue
                if target >= candidates[i]:
                    depth_first_search(candidates[i+1:], target - candidates[i], 
                                       temp_sol + [candidates[i]], sols)
                else:
                    break
                    
        candidates.sort()
        sols = []
        depth_first_search(candidates, target, [], sols)
        
        return sols
        
        
