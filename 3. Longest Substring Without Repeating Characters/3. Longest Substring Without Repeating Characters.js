/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var hash_map = new Map();
    var slen = s.length;
    var maxlen = 0, start = 0;
    
    for (let i = 0; i < slen; i++) {
        var char = s[i];
        if (hash_map.get(char) >= start) {
            start = hash_map.get(char) + 1;
        }
        hash_map.set(char, i);
        if (i - start + 1 > maxlen) {
            maxlen = i - start + 1;
        }
    }
    return maxlen;
};
