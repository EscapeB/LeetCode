/**
 * Created by Chasel on 2017/3/11.
 */
/*
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

    Find all the elements that appear twice in this array.

    Could you do it without extra space and in O(n) runtime?*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    var result=[];
    for(var i=0;i<nums.length;i++){
        var index=Math.abs(nums[i])-1;
        if (nums[index]<0){
            result.push(Math.abs(nums[i]));
        }
        nums[index]=-nums[index];
    }
    return result;
};
console.log(findDuplicates([10,2,5,10,9,1,1,4,3,7]));
