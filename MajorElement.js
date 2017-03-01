/**
 * Created by Chasel on 2016/10/9.
 */
/*
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var temp = nums;
    temp.sort();
    return temp[Math.floor(temp.length / 2)];
};
console.log(majorityElement([1]));