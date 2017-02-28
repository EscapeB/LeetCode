/**
 * Created by Chasel on 2017/2/28.
 */
/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function (n) {
    var output = [];
    for (var i =1; i <= n; i++) {
        var temp = "";
        if (i % 3 == 0 || i % 5 == 0) {
            if (i % 3 == 0) {
                temp += "Fizz";
            }
            if (i % 5 == 0) {
                temp += "Buzz";
            }
            output.push(temp);
        }
        else {
            temp+=i;
            output.push(temp);
        }

    }
    return output;
};
console.log(fizzBuzz(15));