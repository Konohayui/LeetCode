/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// var twoSum = function(nums, target) {
//     var hash_map = {};
    
//     for (let idx = 0; idx < nums.length; idx ++) {
//         const remainder = target - nums[idx];
//         if (remainder in hash_map) {
//             return [hash_map[remainder], idx];
//         }
//         hash_map[remainder] = idx;
//     }
// };
// 

var twoSum = function(nums, target) {
    var hash_map = {};
    for (let idx = 0; idx < nums.length; idx ++) {
        const remainder = target - nums[idx];
        if (remainder in hash_map) {
            return [idx, hash_map[remainder]].reverse();
        }
        hash_map[nums[idx]] = idx;
    }
};

// 
