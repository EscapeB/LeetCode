/**
 * Created by Chasel on 2016/9/27.
 */
var moveZeroes = function (nums) {
    var zeroNumber = 0;
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            nums.splice(i, 1);
            zeroNumber++;
            i--;
        }
    }
    for (var j = 0; j < zeroNumber; j++) {
        nums.push(0);
    }
};
var number = [0, 1, 0, 3, 12];
moveZeroes(number);
console.log(number);