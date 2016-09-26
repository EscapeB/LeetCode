/**
 * Created by Chasel on 2016/9/26.
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
 * @return {TreeNode}
 */
var invertTree = function (root) {
    if (root === null) {
        return null;
    }
    arguments.callee(root.left);
    arguments.callee(root.right);
    var temp = root.left;
    root.left = root.right;
    root.right = temp;
    return root;
};
