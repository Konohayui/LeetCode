class Solution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        total_nums = len(nums)
        if total_nums < 4:
            return []
        else:
            solutions = []
            nums.sort()
            
            for first in range(total_nums-3):
                if first > 0 and nums[first] == nums[first-1]:
                    continue
                elif nums[first] + nums[first+1] + nums[first+2] + nums[first+3] > target:
                    break
                    
                for second in range(first+1, total_nums-2):
                    if second > (first+1) and nums[second] == nums[second-1]:
                        continue
                    elif nums[first] + nums[second] + nums[second+1] + nums[second+2] > target:
                        break
                        
                    third = second + 1
                    forth = total_nums - 1
                    
                    while third < forth:
                        sums = nums[first] + nums[second] + nums[third] + nums[forth]
                        
                        if sums < target:
                            third += 1
                        elif sums > target:
                            forth -= 1
                        else:
                            solutions.append([nums[first], nums[second], nums[third], nums[forth]])
                            while third < forth and nums[third] == nums[third+1]:
                                third += 1
                            third += 1
                            while third < forth and nums[forth] == nums[forth-1]:
                                forth -= 1
                            forth -= 1
                            
            return solutions
