/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort((a, b) => a - b);
    let res = Infinity;
    
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i-1]) {
            continue;
        }
        
        let j = i+1, k = nums.length - 1;
        while (j < k) {
            let total = nums[i] + nums[j] +  nums[k];
            if (Math.abs(target - total) < Math.abs(target - res)) {
                res = total;
            }
            
            if (total < target) {
                j++;
            }
            else if (total > target) {
                k--;
            }
            else {
                return res;
            }
        }
    }
    return res;
};
