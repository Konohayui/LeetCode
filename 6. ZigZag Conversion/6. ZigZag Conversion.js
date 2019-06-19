/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows <= 1) {
        return s;
    }
    
    var res = "";
    var cycle_len = 2*numRows - 2;
    
    for (var i = 0; i < numRows; i++) {
        for (var j = i; j < s.length; j += cycle_len) {
            res += s[j];
            let temp = j + cycle_len - 2*i;
            if (i !== 0 && i !== numRows - 1 && temp < s.length) {
                res += s[temp];
            }
        }
    }
    return res;
};
