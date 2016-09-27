/**
 * Created by Chasel on 2016/9/27.
 */
var moveZeroes = function (nums) {
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            for (var j = i; j < nums.length; j++) {
                if (nums[j] !== 0) {
                    nums[i] = nums[j];
                    nums[j] = 0;
                    break;
                }
            }
        }
    }
};
var number = [0, 1, 0, 3, 12];
console.log(moveZeroes(number));