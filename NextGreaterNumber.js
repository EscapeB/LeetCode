/**
 * Created by Chasel on 2017/3/1.
 */
/**
 * @param {number[]} findNums
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElement = function (findNums, nums) {
    var output = [];
    for (var i = 0; i < findNums.length; i++) {
        var loc = false;
        var find = false;
        for (var j = 0; j < nums.length; j++) {
            if (nums[j] == findNums[i]) {
                loc = true;
            }
            if (loc == true && nums[j] > findNums[i]) {
                find = true;
                output.push(nums[j]);
                break;
            }
        }
        if (!find) {
            output.push(-1);
        }
    }
    return output;
};
console.log(nextGreaterElement([2, 4], [1, 2, 3, 4]));