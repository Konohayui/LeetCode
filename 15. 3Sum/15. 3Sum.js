/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    var res = [];
    
    for (let i = 0; i < nums.length - 2; i++) {
        if (nums[i] > 0) {
            break;
        };
        
        if (i > 0 && nums[i] === nums[i-1]) {
            continue;
        };
        
        let j = i+1, k = nums.length - 1;
        while (j < k) {
            let total = nums[i] + nums[j] + nums[k];
            if (total < 0) {
                j++;
            }
            else if (total > 0) {
                k--;
            }
            else {
                res.push([nums[i], nums[j], nums[k]]);
                while (j < k && nums[j] == nums[j+1]) {
                    j++;
                }
                j++;
                
                while (j < k && nums[k] == nums[k-1]) {
                    k--;
                }
                k--;
            }
        }
    }
    return res;
};
