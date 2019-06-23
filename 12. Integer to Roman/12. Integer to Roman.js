/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    var romans = {"M": 1000,
                  "CM": 900,
                  "D": 500,
                  "CD": 400,
                  "C": 100,
                  "XC": 90,
                  "L": 50,
                  "XL": 40,
                  "X": 10,
                  "IX":9,
                  "V": 5,
                  "IV": 4,
                  "I": 1};
    
    var res = "";
    for (var r in romans) {
        var remainder = parseInt(num/romans[r]);
        res += r.repeat(remainder);
        num %= romans[r];
    }
    
    return res;
};
