/**
 * Created by Chasel on 2016/10/19.
 */
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    var result = [];
    for (var i = 0; i < nums1.length; i++) {
        for (var j = 0; j < nums2.length; j++) {
            if ((nums1[i] ^ nums2[j]) === 0) {
                result.push(nums1[i]);
                nums1.slice(i,1);
                nums2.slice(j,1);
                break;
            }
        }
    }
    return result;

};
console.log(intersect([6,6,4,4,0,0,8,1,2],
    [6]));