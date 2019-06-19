/**
 * @param {string} s
 * @return {string}
 */

var helper = function(s, l, r) {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
        l--;
        r++;
    }
    return s.slice(l+1, r)
}

var longestPalindrome = function(s) {
    var res = "";
    var temp;
    
    for (var i = 0; i< s.length; i++) {
        temp = helper(s, i, i)
        if (temp.length > res.length) {
            res = temp;
        }
        
        temp = helper(s, i, i+1)
        if (temp.length > res.length) {
            res = temp;
        }
    }
    return res;
};
