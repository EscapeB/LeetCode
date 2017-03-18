/**
 * Created by Chasel on 2017/3/18.
 */

/*
 Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

 This is case sensitive, for example "Aa" is not considered a palindrome here*/
/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
    var low = new Array(26);
    var up = new Array(26);
    for (var i=0;i<26;i++){low[i]=up[i]=0;}
    var result = 0;
    for (var i = 0; i < s.length; i++) {
        if (s.charCodeAt(i) - 'a'.charCodeAt(0) >= 0) {
            low[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        }
        else {
            up[s.charCodeAt(i) - 'A'.charCodeAt(0)]++;
        }
    }
    for (var j = 0; j < 26; j++) {
        if (low[j]) {
            result += Math.floor(low[j] / 2) * 2;
        }
        if (up[j]) {
            result += Math.floor(up[j] / 2) * 2;
        }
    }
    result==s.length?result:result++;
    return result;

};
console.log(longestPalindrome("abccccdd"));