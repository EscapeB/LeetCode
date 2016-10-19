/**
 * Created by Chasel on 2016/10/9.
 */
/*
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.*/
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
    var counts = new Array(26);
    for (var i = 0; i < 26; i++) {
        counts[i] = 0;
    }
    for (var i = 0; i < s.length; i++) {
        counts[s.charCodeAt(i) - "a".charCodeAt(0)]++;
    }
    for (var i = 0; i < s.length; i++) {
        if (counts[s.charCodeAt(i) - 'a'.charCodeAt(0)] == 1) {
            return i;
        }
    }
    return -1;
};
console.log(firstUniqChar("loveleetcode"));