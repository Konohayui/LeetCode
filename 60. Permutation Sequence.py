class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = ""
        k -= 1
        
        fact = [1]*n
        for i in range(1, n):
            fact[i] = fact[i-1]*i
            
        for i in range(n):
            idx = int(k / fact[n - i - 1])
            k %= fact[n - i -1]
            res += str(nums[idx])
            nums.pop(idx)
            
        return res
        
