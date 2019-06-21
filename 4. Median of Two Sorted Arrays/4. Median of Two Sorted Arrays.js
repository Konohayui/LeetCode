/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let len1 = nums1.length, len2 = nums2.length;
    if ((len1+len2) % 2 === 1) {
        return getKth(nums1, nums2, parseInt((len1+len2)/2) + 1);
    }
    return (getKth(nums1, nums2, parseInt((len1+len2)/2)) + getKth(nums1, nums2, parseInt((len1+len2)/2) + 1))*0.5
};
    
var getKth = function(nums1, nums2, k) {
    let len1 = nums1.length, len2 = nums2.length;
    if (len1 > len2) {
        return getKth(nums2, nums1, k);
    }
    if (len1 == 0) {
        return nums2[k - 1];
    }
    if (k == 1) {
        return Math.min(nums1[0], nums2[0]);
    }
    let pos1 = Math.min(parseInt(k/2), len1), pos2 = k - pos1;
    if (nums1[pos1- 1] < nums2[pos2 - 1]) {
        return getKth(nums1.slice(pos1), nums2, pos2);
    }
    else {
        return getKth(nums1, nums2.slice(pos2), pos1);
    }
}
