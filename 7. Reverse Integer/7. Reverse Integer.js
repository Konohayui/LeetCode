/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const threshold = Math.pow(2, 31);
    var res = 0;
    
    while (x != 0) {
        let carrier = x%10;
        x = parseInt(x/10);
        if (res > threshold/10 || (res == threshold/10 && carrier > 7)) {
            return 0;
        }
        else if (res < -threshold/10 || (res == -threshold/10 && carrier < -8)) {
            return 0;
        }
        res = res*10 + carrier;
    }
    return res;
};
