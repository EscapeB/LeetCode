/**
 * Created by Chasel on 2017/3/2.
 */
/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function (n) {
    if (n === 0) {
        return 1;
    }
    else if (n === 1) {
        return 10;
    }
    var m = 1;
    for (var i = 10; i > 10 - n; i--) {
        if (i == 10) {
            m *= 9;
        }
        else {
            m *= i;
        }
    }
    return m + countNumbersWithUniqueDigits(n - 1);

};
console.log(countNumbersWithUniqueDigits(0));
