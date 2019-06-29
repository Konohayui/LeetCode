/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const digit_map = {"1": "*",
                       "2": "abc",
                       "3": "def",
                       "4": "ghi",
                       "5": "jkl",
                       "6": "mno",
                       "7": "pqrs",
                       "8": "tuv",
                       "9": "wxyz"}
    
    let queue = digits.length === 0 ? []:[""];
    let letters, queueLength, itemFromQueue;
    
    for (var i = 0; i < digits.length; i++) {
        letters = digit_map[digits[i]];
        queueLength = queue.length;
        
        for (var j = 0; j < queueLength; j++) {
            itemFromQueue = queue.shift();
            for (var k = 0; k < letters.length; k++) {
                queue.push(itemFromQueue + letters[k])
            }
        }
    }
    return queue;
};

