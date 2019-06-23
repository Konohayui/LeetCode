/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var romans = {"M": 1000,
                  "D": 500,
                  "C": 100,
                  "L": 50,
                  "X": 10,
                  "V": 5,
                  "I": 1};
    
    var res = 0;
    var len = s.length;
    for (let i = 0; i < len - 1; i++) {
        if (romans[s[i]] < romans[s[i+1]]) {
            res -= romans[s[i]];
        }
        else {
            res += romans[s[i]]; 
        }
    }
    
    res += romans[s[len - 1]]
    return res;
};
