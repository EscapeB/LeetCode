/**
 * Created by Chasel on 2017/1/15.
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var index=0;
    var maxConsecutive=0,max=0;
    while(index<nums.length){
        if (nums[index]==1){
            max++;
            if (index==nums.length-1){
                if (max>maxConsecutive){
                    maxConsecutive=max;
                }
            }
        }
        else {
            if (max>maxConsecutive){
                maxConsecutive=max;
            }
            max=0;
        }
        index++;
    }
    return maxConsecutive;
};
console.log(findMaxConsecutiveOnes([1,1,0,1,1,1]));
