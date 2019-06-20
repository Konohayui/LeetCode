/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }
    x = x.toString();
    var start = 0, end = x.length - 1;
    while (start < end) {
        if (x.charAt(start++) != x.charAt(end--)) {
            return false;
        }
    }
    return true;
};
