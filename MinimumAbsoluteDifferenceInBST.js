/**
 * Created by Chasel on 2017/3/2.
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}
var getMinimumDifference = function (root) {
    var min = Number.MAX_VALUE;
    var numbers = [];
    console.log(root.right.val);
    var visitTree = function (node) {
        if (node == null) {
            return;
        }
        else if (node.left == null && node.right == null) {
            return node.val;
        }
        else {
            var left = visitTree(node.left);
            if ((typeof left) != "undefined") {
                numbers.push(left);
            }
            numbers.push(node.val);
            var right = visitTree(node.right);
            if ((typeof right) != "undefined") {
                numbers.push(right);
            }
        }
    }
    visitTree(root);
    for (var i = 0; i < numbers.length - 1; i++) {
        var difference = numbers[i + 1] - numbers[i];
        if (difference <= min) {
            min = difference;
        }
    }
    return min;

};
var root = new TreeNode(1);
root.left = null;
root.right = new TreeNode(3);
root.right.left = new TreeNode(2);
console.log(getMinimumDifference(root));