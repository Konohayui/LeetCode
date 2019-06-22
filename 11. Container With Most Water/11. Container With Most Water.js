/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var max_area = 0, left = 0, right = height.length - 1;
    
    while (left < right) {
        const width = right - left;
        max_area = Math.max(max_area, width*Math.min(height[left], height[right]))
        if (height[left] < height[right]) {
            left++;
        }
        else {
            right--;
        }
    }
    return max_area;
};
