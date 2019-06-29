class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        total_nums = len(nums)
        if total_nums == 3:
            return sum(nums)
        else:
            solution = 0
            diff = 999999999
            nums.sort()
            
            for i in range(total_nums-2):
                j = i + 1
                k = total_nums - 1
                
                while j < k:
                    sums = nums[i] + nums[j] + nums[k]
                    
                    if sums == target:
                        return sums
                    else:
                        if abs(target - sums) < diff:
                            diff = abs(target - sums)
                            solution = sums
                        if sums < target:
                            j += 1
                        elif sums > target :
                            k -= 1
                    
            return solution
