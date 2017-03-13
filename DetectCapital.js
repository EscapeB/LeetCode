/**
 * Created by Chasel on 2017/3/13.
 */
/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function (word) {
    var firstPattern = true;
    var allPattern = true;
    if (word.charAt(0) > 'Z' || word.charAt(0) < 'A') {
        for (var i = 1; i < word.length; i++) {
            if (word.charAt(i) < 'a' || word.charAt(i) > 'z') {
                allPattern = false;
            }
        }
        if (allPattern) {
            return true
        }
        else {
            return false;
        }
    }
    else {
        for (var i = 1; i < word.length; i++) {
            if (word.charAt(i) > 'Z' || word.charAt(i) < 'A') {
                firstPattern = false;
            }
            else {
                allPattern = false;
            }
        }
        if (firstPattern || allPattern) {
            return true;
        }
        else {
            return false;
        }
    }
};
console.log(detectCapitalUse("g"));