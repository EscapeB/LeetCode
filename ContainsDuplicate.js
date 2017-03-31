/**
 * Created by Chasel on 2017/3/31.
 */
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var flags=[];
    for (var i=0;i<nums.length;i++){
        if (typeof flags[nums[i]] !=='undefined'){
            return true;

        }
        else {
            flags[nums[i]]=true;
        }
    }
    return false;
};
console.log(containsDuplicate([1,2,3,1]));