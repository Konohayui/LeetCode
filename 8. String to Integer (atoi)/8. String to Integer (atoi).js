/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    var i = 0, sign = 1, res = 0;
    
    while(str[i] === " ") {
        i += 1;
    }
    
    if (str[i] === "+") {
        i += 1;
        sign = sign;
    }
    else if (str[i] === "-") {
        i += 1;
        sign = -1;
    }
    
    for (; i < str.length; i++) {
        const code = str.charCodeAt(i) - 48; //"0" = 48
        if (code < 0 || code > 9) {
            break;
        }
        res = res*10 + code;
    }

    res = sign*res;
    return Math.max(-(2**31)-1, Math.min(2**31, res));
};
