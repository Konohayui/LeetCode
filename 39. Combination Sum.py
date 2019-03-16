class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def depth_first_search(candidates, target, temp_sol, sols):
            if target == 0:
                sols.append(temp_sol)
                
                return
        
            for i in range(len(candidates)):
                if target >= candidates[i]:
                    depth_first_search(candidates[i:], target - candidates[i], 
                                       temp_sol + [candidates[i]], sols)

                else:
                    break
                    
        candidates.sort()
        sols = []
        depth_first_search(candidates, target, [], sols)
        
        return sols
        
        
        
