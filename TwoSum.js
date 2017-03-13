/**
 * Created by Chasel on 2017/3/13.
 */
/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
    var maxIndex;
    var index1;
    var index2;
    for (var i = 0; i < numbers.length; i++) {
        for (var j = i; j < numbers.length; j++) {
            if ((numbers[i] + numbers[j]) === target&&i!=j) {
                index1 = i;
                index2 = j;
                break;
            }
        }
    }
    return [index1+1, index2+1];
};
console.log(twoSum([-1,0],-1));