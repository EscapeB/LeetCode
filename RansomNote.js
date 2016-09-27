/**
 * Created by Chasel on 2016/9/27.
 */
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
    var flag = new Array(magazine.length);
    for (var i = 0; i < flag.length; i++) {
        flag[i] = 0;
    }
    for (var j = 0; j < ransomNote.length; j++) {
        var sign = false;
        for (var k = 0; k < magazine.length; k++) {
            if (ransomNote[j] == magazine[k] && flag[k] != 1) {
                sign = true;
                flag[k] = 1;
                break;
            }
        }
        if (sign == false) {
            return false;
        }
    }
    return true;
};
console.log(canConstruct("aa", "ab"));