/**
 * Created by Chasel on 2017/3/11.
 */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
/*Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

    Find all the elements of [1, n] inclusive that do not appear in this array.

    Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

    Example:

Input:
    [4,3,2,7,8,2,3,1]

Output:
    [5,6]*/
var findDisappearedNumbers = function(nums) {
    var result=[];
    for (var i=0;i<nums.length;i++){
        var index=Math.abs(nums[i])-1;
        if (nums[index]>0){
            nums[index]=-nums[index];
        }
    }
    for (var i=0;i<nums.length;i++){
        if (nums[i]>0){
            result.push(i+1);
        }
    }
    return result;
};
console.log(findDisappearedNumbers([4,3,2,7,5,2,3,1]));
