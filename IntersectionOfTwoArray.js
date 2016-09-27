/**
 * Created by Chasel on 2016/9/27.
 */
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
    var intersection = [];
    while (nums1.length > 0) {
        var temp = nums1.pop();
        if (nums2.indexOf(temp) >= 0 && intersection.indexOf(temp) < 0) {
            intersection.push(temp)
        }
    }
    return intersection;
};
console.log(intersection([1, 3, 3, 4], [1, 4, 2, 4, 3]));