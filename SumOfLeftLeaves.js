/**
 * Created by Chasel on 2016/9/27.
 */
/**
 Definition for a binary tree node.
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumOfLeftLeaves = function (root) {

    var sum = 0;
    sum = leftSum(root, false);
    function leftSum(node, isLeft) {
        if (node === null) {
            return 0
        }
        if (node.left === null && node.right === null && isLeft) {
            return node.val;
        }
        return arguments.callee(node.left, true) + arguments.callee(node.right, false);
    }

    return sum;

};
var root = new TreeNode(0);
root.left = new TreeNode(1);
root.right = new TreeNode(2);
//root.left.left = new TreeNode(3);
//root.left.right = new TreeNode(4);
root.right.left = new TreeNode(5);
//root.left.left.left = new TreeNode(6);
console.log(sumOfLeftLeaves([3, 9, 20, null, null, 15, 7]));