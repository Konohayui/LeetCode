class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        total_nums = len(nums)
        if total_nums == 0:
            return []
        else:
            solutions = []
            nums.sort()
            
            for i in range(total_nums - 2):
                if nums[i] > 0:
                    break
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                j = i + 1
                k = total_nums - 1
                
                while j < k:
                    sums = nums[i] + nums[j] + nums[k]
                    if sums < 0:
                        j += 1
                    elif sums > 0:
                        k -= 1
                    else:
                        solutions.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        j += 1
                        
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        k -= 1
                        
            return solutions
