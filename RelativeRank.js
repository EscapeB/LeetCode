/**
 * Created by Chasel on 2017/3/13.
 */
/**
 * @param {number[]} nums
 * @return {string[]}
 */
var findRelativeRanks = function(nums) {
    var result=nums.concat();
    for (var i=0;i<nums.length;i++){
        var index=nums.indexOf(Math.max.apply(Math,nums));
        if (i==0){
            result[index]="Gold Medal";
            nums[index]=-nums[index];
        }
        else if (i==1){
            result[index]="Silver Medal";
            nums[index]=-nums[index];
        }
        else if(i==2){
            result[index]="Bronze Medal";
            nums[index]=-nums[index];
        }
        else {
            result[index]=(i+1).toString();
            nums[index]=-nums[index];
        }
    }
    return result;
};
console.log(findRelativeRanks([5,4,3,2,1]));